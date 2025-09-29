# -*- coding: utf-8 -*-

# Copyright 2024 Wen-Chin Huang
#  MIT License (https://opensource.org/licenses/MIT)

# RAMP simple model

import math
import time

import numpy as np
import sheet.models
import torch
import torch.nn as nn
from sheet.modules.utils import make_non_pad_mask
from sheet.nonparametric.datastore import Datastore


class RAMPSimple(torch.nn.Module):
    def __init__(
        self,
        model_input: str,
        # parametric model related
        parametric_model_type: str,
        parametric_model_params,
        parametric_model_inference_mode: str,
        # datastore related
        datastore: Datastore = None,
        # k-net related
        k: int = 60,
        k_net_dim: int = 128,
        # lambda-net related
        lambda_net_type: str = "original",
        lambda_net_dim: int = 128,
        # common to all models
        num_domains: int = None,
        num_listeners: int = None,
    ):
        super().__init__()  # this is needed! or else there will be an error.
        self.k = k
        self.datastore = datastore

        # define parametric model
        parametric_model_class = getattr(sheet.models, parametric_model_type)
        self.parametric_model = parametric_model_class(
            model_input,
            num_listeners=num_listeners,
            num_domains=num_domains,
            **parametric_model_params
        )
        self.parametric_model_inference_mode = parametric_model_inference_mode

        # define k-net
        self.k_net = nn.Sequential(
            nn.Linear(k, k_net_dim),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(k_net_dim, k),
            nn.Softmax(),
        )

        # define lambda-net
        self.lambda_net_type = lambda_net_type
        if lambda_net_type == "original":
            self.lambda_net = nn.Sequential(
                nn.Linear(2 + self.k, lambda_net_dim),
                nn.ReLU(),
                nn.Dropout(0.3),
                nn.Linear(lambda_net_dim, 2),
                nn.Softmax(),
            )
        elif lambda_net_type == "easy":
            self.lambda_net = nn.Sequential(nn.Linear(2, 2), nn.Softmax())
        else:
            raise NotImplementedError

    def get_num_params(self):
        return sum(p.numel() for n, p in self.named_parameters())

    def parametric_model_inference(self, inputs):
        with torch.no_grad():
            if self.parametric_model_inference_mode == "mean_listener":
                outputs = self.parametric_model.mean_listener_inference(inputs)
            elif self.parametric_model_inference_mode == "mean_net":
                outputs = self.parametric_model.mean_net_inference(inputs)
            else:
                raise NotImplementedError

        return outputs

    def nonparametric_model_inference(self, hs):
        device = hs.device
        hs = torch.mean(hs, dim=1)

        # get kNN neighbots and np score
        # start_time = time.time()
        knn_search_results = self.datastore.knn(
            hs.detach().cpu().numpy(), self.k, search_only=True
        )
        # print("knn search time", time.time() - start_time)
        knn_distances = torch.tensor(
            knn_search_results["distances"], dtype=torch.float, device=device
        )
        knn_scores = torch.tensor(
            knn_search_results["scores"], dtype=torch.float, device=device
        )
        weights = self.k_net(knn_distances)
        np_scores = torch.sum(weights * knn_scores, axis=1)

        return {"np_scores": np_scores, "knn_distances": knn_distances}

    def lambda_net_forward(self, p_scores, np_scores, knn_distances):
        if self.lambda_net_type == "original":
            lambdas = self.lambda_net(
                torch.cat(
                    [p_scores.unsqueeze(1), np_scores.unsqueeze(1), knn_distances],
                    dim=1,
                )
            )
        elif self.lambda_net_type == "easy":
            lambdas = self.lambda_net(
                torch.cat([p_scores.unsqueeze(1), np_scores.unsqueeze(1)], dim=1)
            )
        else:
            raise NotImplementedError
        final_scores = torch.sum(
            torch.stack([p_scores, np_scores], dim=1) * lambdas, dim=1, keepdim=True
        )  # [batch, 1]
        return final_scores

    def forward(self, inputs):
        """Calculate forward propagation.
        Args:
            inputs: dict, which has the following keys:
                - waveform has shape (batch, time)
                - waveform_lengths has shape (batch)
                - listener_ids has shape (batch)
                - domain_ids has shape (batch)
        """
        # get parametric outputs
        # start_time = time.time()
        parametric_outputs = self.parametric_model_inference(inputs)
        p_scores = parametric_outputs["scores"]
        hs = parametric_outputs["ssl_embeddings"]
        # print("parametric time", time.time() - start_time)

        # get nonparametric outputs
        start_time = time.time()
        np_outputs = self.nonparametric_model_inference(hs)
        np_scores = np_outputs["np_scores"]
        print("nonparametric time", time.time() - start_time)

        # lambda-net forward
        final_scores = self.lambda_net_forward(
            p_scores, np_scores, np_outputs["knn_distances"]
        )

        # set outputs
        ret = {}
        ret["mean_scores"] = final_scores

        return ret

    def inference(self, inputs, mode):
        if mode == "fusion":
            return {"scores": self.forward(inputs)["mean_scores"].squeeze(-1)}
        else:
            raise NotImplementedError

    def mean_listener_inference(self, inputs):
        waveform, waveform_lengths = inputs["waveform"], inputs["waveform_lengths"]
        batch = waveform.size(0)

        # ssl model forward
        ssl_model_outputs, ssl_model_output_lengths = self.ssl_model_forward(
            waveform, waveform_lengths
        )
        to_concat = [ssl_model_outputs]
        time = ssl_model_outputs.size(1)

        # get listener embedding
        if self.use_listener_modeling:
            device = waveform.device
            listener_ids = (
                torch.ones(batch, dtype=torch.long) * self.num_listeners - 1
            ).to(
                device
            )  # (bs)
            listener_embs = self.listener_embeddings(listener_ids)  # (batch, emb_dim)
            listener_embs = torch.stack(
                [listener_embs for i in range(time)], dim=1
            )  # (batch, time, feat_dim)

            # NOTE(unilight): is this needed?
            # encoder_outputs = encoder_outputs.view(
            # (batch, time, -1)
            # )  # (batch, time, feat_dim)
            to_concat.append(listener_embs)

        # get domain embedding
        if self.use_domain_modeling:
            device = waveform.device
            assert "domain_idxs" in inputs, "Must specify domain ID even in inference."
            domain_ids = inputs["domain_idxs"]
            domain_embs = self.domain_embeddings(domain_ids)  # (batch, emb_dim)
            domain_embs = torch.stack(
                [domain_embs for i in range(time)], dim=1
            )  # (batch, time, feat_dim)

            # NOTE(unilight): is this needed?
            # encoder_outputs = encoder_outputs.view(
            # (batch, time, -1)
            # )  # (batch, time, feat_dim)
            to_concat.append(domain_embs)

        decoder_inputs = torch.cat(to_concat, dim=2)

        # decoder rnn
        if self.use_decoder_rnn:
            decoder_inputs, (h, c) = self.decoder_rnn(decoder_inputs)

        # decoder dnn
        decoder_outputs = self.decoder_dnn(
            decoder_inputs
        )  # [batch, time, 1 (scalar) / 5 (categorical)]

        scores = torch.mean(decoder_outputs.squeeze(-1), dim=1)
        return {"scores": scores}

    def ssl_model_forward(self, waveform, waveform_lengths):
        all_ssl_model_outputs, all_ssl_model_output_lengths = self.ssl_model(
            waveform, waveform_lengths
        )
        ssl_model_outputs = all_ssl_model_outputs[self.ssl_model_layer_idx]
        ssl_model_output_lengths = all_ssl_model_output_lengths[
            self.ssl_model_layer_idx
        ]
        return ssl_model_outputs, ssl_model_output_lengths

    def get_ssl_embeddings(self, inputs):
        waveform = inputs["waveform"]
        waveform_lengths = inputs["waveform_lengths"]

        all_encoder_outputs, all_encoder_outputs_lens = self.ssl_model(
            waveform, waveform_lengths
        )
        encoder_outputs = all_encoder_outputs[self.ssl_model_layer_idx]
        return encoder_outputs
