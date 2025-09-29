# -*- coding: utf-8 -*-

# Copyright 2024 Wen-Chin Huang
#  MIT License (https://opensource.org/licenses/MIT)

# RAMP model
# modified from: https://github.com/NKU-HLT/RAMP_MOS (written by Hui Wang)


import time

import sheet.models
import torch
import torch.nn as nn
from sheet.nonparametric.datastore import Datastore


class RAMP(torch.nn.Module):
    def __init__(
        self,
        model_input: str,
        # parametric model related
        parametric_model_type: str,
        parametric_model_params,
        parametric_model_inference_mode: str,
        # datastore related
        datastore: Datastore,
        # categorical head related
        categorical_head_output_dim: int = 17,
        categorical_head_output_step: float = 0.25,
        # k-net related
        max_k: int = 60,
        top_k: int = 8,
        # k: int = 60,
        k_net_dim: int = 32,
        # lambda-net related
        # lambda_net_type: str = "original",
        lambda_net_dim: int = 32,
        # special option
        use_confidence: bool = True,
        # common to all models
        num_domains: int = None,
        num_listeners: int = None,
    ):
        super().__init__()  # this is needed! or else there will be an error.
        self.max_k = max_k
        self.top_k = top_k
        self.datastore = datastore
        self.categorical_head_output_dim = categorical_head_output_dim
        self.categorical_head_output_step = categorical_head_output_step
        self.use_confidence = use_confidence

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
            nn.Linear(max_k, k_net_dim),
            nn.Tanh(),
            nn.Dropout(0.2),
            nn.Linear(k_net_dim, max_k),
            nn.Softmax(),
        )

        # define lambda-net
        # not sure why the original implementation used two lambda nets
        self.lambda_net_from_knn = nn.Sequential(
            nn.Linear(max_k, lambda_net_dim),
            nn.Tanh(),
            nn.Dropout(p=0.2),
            nn.Linear(lambda_net_dim, 1),
        )
        if use_confidence:
            lambda_net_from_wav_input_dim = max_k + top_k + 2
        else:
            lambda_net_from_wav_input_dim = max_k
        self.lambda_net_from_wav = nn.Sequential(
            nn.Linear(lambda_net_from_wav_input_dim, lambda_net_dim),
            nn.Tanh(),
            nn.Dropout(p=0.2),
            nn.Linear(lambda_net_dim, 1),
        )

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

        # take mean over the time axis
        hs = torch.mean(hs, dim=1)

        # get kNN neighbors and np score
        # start_time = time.time()
        knn_search_results = self.datastore.knn(
            hs.detach().cpu().numpy(), self.max_k, search_only=True
        )
        # print("knn search time", time.time() - start_time)
        knn_distances = torch.tensor(
            knn_search_results["distances"], dtype=torch.float, device=device
        )
        knn_scores = torch.tensor(
            knn_search_results["scores"], dtype=torch.float, device=device
        )

        # forward k-net
        weights = self.k_net(knn_distances)
        np_scores = torch.sum(weights * knn_scores, axis=1)

        return {"np_scores": np_scores, "knn_distances": knn_distances}

    def get_bin_index(self, x):
        """
        Turn scalar values to bin index.
        For instance, if we have MOS=4, then 4-1 * (1 / 0.25) = 3 * 4 = 12th bin
        """
        x_idx = (x - 1) * (1 / self.categorical_head_output_step)
        x_idx = torch.clamp(x_idx, 0, 1 / self.categorical_head_output_step * 4)
        return x_idx.to(torch.int64)

    def lambda_net_forward(self, p_scores, np_scores, knn_distances, confidences=None):
        # forward: lambda net for knn
        knn_lambda = self.lambda_net_from_knn(knn_distances)  # [B,X,1]

        # forward: lambda net for wav (=parametric input)
        if confidences is not None:
            # take mean over the time axis: [B, T, bin_steps] -> [B, bin_steps]
            confidences = torch.mean(confidences, dim=1)
            
            # get which bins S_r and S_p are in
            s_r_idx = self.get_bin_index(p_scores)  # [B]
            s_p_idx = self.get_bin_index(np_scores)  # [B]

            # concat (1) confidence of top k scores (2) confidence of S_r and S_p
            idx = torch.cat((s_r_idx.unsqueeze(-1), s_p_idx.unsqueeze(-1)), dim=-1)  # [B,2]
            s_r_s_p_confidence = torch.gather(confidences, dim=-1, index=idx)  # [B,X,2]
            top_k_confidence, _ = torch.topk(confidences, self.top_k)  # [B,X,top_k]
            all_confidences = torch.cat(
                (s_r_s_p_confidence, top_k_confidence), dim=-1
            )  # [B,X,2+top_k]

            lambda_net_from_wav_input = torch.cat((all_confidences, knn_distances), dim=-1)
        else:
            lambda_net_from_wav_input = knn_distances

        # true forward
        wav_lambda = self.lambda_net_from_wav(lambda_net_from_wav_input)

        # get final score (= weighted sum using the two lambdas and p_scores, np_scores)
        _lambda = torch.softmax(
            torch.cat((knn_lambda, wav_lambda), dim=-1), -1
        )  # [B,X,2]
        final_scores = _lambda[:, 0] * np_scores + _lambda[:, 1] * p_scores
        return final_scores, _lambda

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
        parametric_outputs = self.parametric_model_inference(inputs)
        p_scores = parametric_outputs["scores"]
        hs = parametric_outputs["ssl_embeddings"]
        if self.use_confidence:
            confidences = parametric_outputs["confidences"]
        else:
            confidences = None

        # get nonparametric outputs (= k-net outputs)
        np_outputs = self.nonparametric_model_inference(hs)
        np_scores = np_outputs["np_scores"]
        knn_distances = np_outputs["knn_distances"]

        # lambda-net forward
        final_scores, _lambda = self.lambda_net_forward(
            p_scores, np_scores, knn_distances, confidences
        )
        final_scores = final_scores.unsqueeze(
            1
        )  # the loss class demands the scores to be shape [batch, time, 1]

        # set outputs
        ret = {}
        ret["mean_scores"] = final_scores
        ret["p_scores"] = p_scores
        ret["np_scores"] = np_scores
        ret["lambda_np"] = _lambda[:, 0]
        ret["lambda_p"] = _lambda[:, 1]

        return ret

    def inference(self, inputs, mode):
        if mode == "fusion":
            model_outputs = self.forward(inputs)
            return {
                "scores": model_outputs["mean_scores"].squeeze(-1),
                "lambda_p": model_outputs["lambda_p"],
                "lambda_np": model_outputs["lambda_np"],
                "p_scores": model_outputs["p_scores"],
                "np_scores": model_outputs["np_scores"],
            }
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
