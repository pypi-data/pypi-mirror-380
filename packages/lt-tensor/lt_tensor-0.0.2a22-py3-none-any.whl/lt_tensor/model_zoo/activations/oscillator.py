import math
import torch

from torch import nn, Tensor
from .basic_utils import _ActivationBase

from .base import ScaleMinMax
from typing import Callable
from torch.nn import functional as F


class Oscillator(_ActivationBase):
    def __init__(
        self,
        base: float = 1.0,
        radius: float = 1.44,
        signal: float = 64.0,
        sig_range: float = 8,
        requires_grad: bool = False,
    ):
        super().__init__()
        self.base = nn.Parameter(
            torch.tensor(float(base), dtype=torch.float32), requires_grad=requires_grad
        )
        self.signal = self.base = nn.Parameter(
            torch.tensor(float(signal), dtype=torch.float32),
            requires_grad=requires_grad,
        )
        self.range = self.base = nn.Parameter(
            torch.tensor(float(sig_range), dtype=torch.float32),
            requires_grad=requires_grad,
        )
        self.radius = nn.Parameter(
            torch.tensor(radius / math.pi, dtype=torch.float32),
            requires_grad=requires_grad,
        )
        self._hf_pi = math.pi / 2

    def reset_parameters(self):
        raise RuntimeError(
            "This module does not support reseting/initialization of parameters!"
        )

    def _clamp_values(self, x: Tensor):
        cos_x = x.cos()
        return torch.max(
            torch.min(self.base, cos_x),
            torch.max(cos_x, torch.sin(0.5 * x * self._hf_pi)),
        )

    def _get_curves(self, x: Tensor):
        radius = self.radius.sin().sqrt() / self.range
        scaled = self.signal * radius * x.cos()
        return self._clamp_values(scaled)

    def forward(self, x: Tensor):
        return self._get_curves(x)


class SquaredOscillatorMul(Oscillator):
    def __init__(
        self,
        base: float = 1.0,
        radius: float = 1.44,
        signal: float = 64.0,
        sig_range: float = 8,
        requires_grad: bool = False,
        dim: int = -1,
        gated_activ: Callable[[Tensor], Tensor] = F.tanh,
    ):
        super().__init__(base, radius, signal, sig_range, requires_grad)
        self.scale_sq = ScaleMinMax(0, math.pi**2, dim=dim)
        self._fc = gated_activ

    def forward(self, x: Tensor):
        scaled = self.scale_sq(super().forward(x)).sqrt()
        return x * (1.0 + self._fc(scaled))


class SquaredOscillatorSum(Oscillator):
    def __init__(
        self,
        base: float = 1.0,
        radius: float = 1.44,
        signal: float = 64.0,
        sig_range: float = 8,
        requires_grad: bool = False,
        dim: int = -1,
    ):
        super().__init__(base, radius, signal, sig_range, requires_grad)
        self.scale_sq = ScaleMinMax(0, math.pi**2, dim=dim)

    def forward(self, x: Tensor):
        scaled = self.scale_sq(super().forward(x)).sqrt()
        return x + scaled


class OscillatorSum(Oscillator):
    def forward(self, x: Tensor):
        return x + super().forward(x)


class OscillatorMul(Oscillator):
    def __init__(
        self,
        base: float = 1.0,
        radius: float = 1.44,
        signal: float = 64.0,
        sig_range: float = 8,
        requires_grad: bool = False,
        gated_activ: Callable[[Tensor], Tensor] = F.tanh,
    ):
        super().__init__(base, radius, signal, sig_range, requires_grad)
        self._fc = gated_activ

    def forward(self, x: Tensor):
        return x * (1.0 + self._fc(super().forward(x)))
