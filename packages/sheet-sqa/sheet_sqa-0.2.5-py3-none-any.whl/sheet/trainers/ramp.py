#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright 2024 Wen-Chin Huang
#  MIT License (https://opensource.org/licenses/MIT)

import logging
import os

# set to avoid matplotlib error in CLI environment
import matplotlib
import torch
from sheet.trainers.non_intrusive import NonIntrusiveEstimatorTrainer
from sheet.utils.model_io import (
    filter_modules,
    get_partial_state_dict,
    print_new_keys,
    transfer_verification,
)

matplotlib.use("Agg")
import matplotlib.pyplot as plt


class RAMPTrainer(NonIntrusiveEstimatorTrainer):
    """Customized trainer module for RAMP."""

    def load_parametric_model(self, checkpoint_path):
        if self.config["distributed"]:
            main_state_dict = self.model.module.state_dict()
        else:
            main_state_dict = self.model.state_dict()

        if os.path.isfile(checkpoint_path):
            model_state_dict = torch.load(checkpoint_path, map_location="cpu")["model"]

            # prepend "parametric_model" in all keys
            partial_state_dict = {
                "parametric_model." + k: v for k, v in model_state_dict.items()
            }

            for k in partial_state_dict.keys():
                logging.warning(f"Overriding module {k}")
            main_state_dict.update(partial_state_dict)

        else:
            logging.error(f"Specified model was not found: {checkpoint_path}")
            exit(1)

        if self.config["distributed"]:
            self.model.module.load_state_dict(main_state_dict)
        else:
            self.model.load_state_dict(main_state_dict)

    @torch.no_grad()
    def _eval_step(self, batch):
        """Evaluate model one step."""

        # set up model input
        inputs = {
            self.config["model_input"]: batch[self.config["model_input"]].to(
                self.device
            ),
            self.config["model_input"]
            + "_lengths": batch[self.config["model_input"] + "_lengths"].to(
                self.device
            ),
        }
        if "domain_idxs" in batch:
            inputs["domain_idxs"] = batch["domain_idxs"].to(self.device)
        if "phoneme_idxs" in batch:
            inputs["phoneme_idxs"] = batch["phoneme_idxs"].to(self.device)
            inputs["phoneme_lengths"] = batch["phoneme_lengths"]
        if "reference_idxs" in batch:
            inputs["reference_idxs"] = batch["reference_idxs"].to(self.device)
            inputs["reference_lengths"] = batch["reference_lengths"]

        # model forward
        outputs = self.model.inference(inputs, self.config["inference_mode"])

        # construct the eval_results dict
        pred_mean_scores = outputs["scores"].cpu().detach().numpy()
        true_mean_scores = batch["avg_scores"].numpy()
        self.eval_results["pred_mean_scores"].extend(pred_mean_scores.tolist())
        self.eval_results["true_mean_scores"].extend(true_mean_scores.tolist())
        sys_names = batch["system_ids"]
        for j, sys_name in enumerate(sys_names):
            self.eval_sys_results["pred_mean_scores"][sys_name].append(
                pred_mean_scores[j]
            )
            self.eval_sys_results["true_mean_scores"][sys_name].append(
                true_mean_scores[j]
            )
