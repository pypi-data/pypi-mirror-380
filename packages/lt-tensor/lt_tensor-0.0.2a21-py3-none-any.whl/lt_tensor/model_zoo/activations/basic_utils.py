import math
import torch
from abc import ABC
from torch import nn, Tensor
from lt_tensor.model_base import Model


class _ActivationBase(Model, ABC):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwds) -> Tensor:
        return super().__call__(*args, **kwds)

    def reset_parameters(self):
        for param in self.parameters():
            sz = param.size(0) if param.ndim == 1 else max(list(param.shape))
            bound = 1 / (1.0 + math.sqrt(sz))
            nn.init.uniform_(param, -bound, bound)

    def forward(self, x: Tensor, *args, **kwargs) -> Tensor:
        raise NotImplementedError()
