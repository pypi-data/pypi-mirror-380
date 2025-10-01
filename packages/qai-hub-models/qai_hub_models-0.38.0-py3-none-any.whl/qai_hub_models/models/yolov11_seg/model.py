# ---------------------------------------------------------------------
# Copyright (c) 2025 Qualcomm Technologies, Inc. and/or its subsidiaries.
# SPDX-License-Identifier: BSD-3-Clause
# ---------------------------------------------------------------------

from __future__ import annotations

from typing import cast

import torch
from ultralytics import YOLO as ultralytics_YOLO
from ultralytics.nn.tasks import SegmentationModel

from qai_hub_models.models._shared.yolo.model import YoloSeg, yolo_segment_postprocess

MODEL_ASSET_VERSION = 1
MODEL_ID = __name__.split(".")[-2]


SUPPORTED_WEIGHTS = [
    "yolo11n-seg.pt",
    "yolo11s-seg.pt",
    "yolo11m-seg.pt",
    "yolo11l-seg.pt",
    "yolo11x-seg.pt",
]
DEFAULT_WEIGHTS = "yolo11n-seg.pt"


class YoloV11Segmentor(YoloSeg):
    """Exportable YoloV11 segmentor, end-to-end."""

    def __init__(self, model: SegmentationModel):
        super().__init__(model)
        self.num_classes: int = model.nc

    @classmethod
    def from_pretrained(cls, ckpt_name: str = DEFAULT_WEIGHTS):
        if ckpt_name not in SUPPORTED_WEIGHTS:
            raise ValueError(
                f"Unsupported checkpoint name provided {ckpt_name}.\n"
                f"Supported checkpoints are {list(SUPPORTED_WEIGHTS)}."
            )
        model = cast(SegmentationModel, ultralytics_YOLO(ckpt_name).model)
        return cls(model)

    def forward(self, image: torch.Tensor):
        """
        Run YoloV11 on `image`, and produce a predicted set of bounding boxes and associated class probabilities.

        Parameters:
            image: Pixel values pre-processed for encoder consumption.
                    Range: float[0, 1]
                    3-channel Color Space: RGB

        Returns:
        boxes: torch.Tensor
            Bounding box locations. Shape is [batch, num preds, 4] where 4 == (x1, y1, x2, y2)
        scores: torch.Tensor
            Class scores multiplied by confidence: Shape is [batch, num_preds]
        masks: torch.Tensor
            Predicted masks: Shape is [batch, num_preds, 32]
        classes: torch.Tensor
            Shape is [batch, num_preds] where the last dim is the index of the most probable class of the prediction.
        protos: torch.Tensor
            Tensor of shape[batch, 32, mask_h, mask_w]
            Multiply masks and protos to generate output masks.
        """
        predictions = self.model(image)
        boxes, scores, masks, classes = yolo_segment_postprocess(
            predictions[0], self.num_classes
        )
        return boxes, scores, masks, classes.to(torch.uint8), predictions[1][-1]
