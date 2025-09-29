import math
import torch

from torch import nn, Tensor
from .basic_utils import _ActivationBase
from typing import Union, Sequence


class Hermite(_ActivationBase):
    def __init__(self, degree: int, requires_grad: bool = True):
        super().__init__()
        degree = int(degree)
        assert (
            degree >= 1
        ), f"degree must be equal or larger than 1, received instead: {degree}"
        self.degree = degree
        # Learnable coefficients for each polynomial degree
        self.coeffs = nn.Parameter(torch.ones(degree + 1), requires_grad=requires_grad)
        self.step_ld = 1.0 / (math.sqrt(degree) * math.pi)

        self.reset_parameters()

    def forward(self, x):
        H = [torch.ones_like(x), 2 * x]  # H0 and H1

        for n in range(2, self.degree + 1):
            Hn = 2 * x * H[-1] - 2 * (n - 1) * H[-2]
            H.append(Hn * self.step_ld)
        H_stack = torch.stack(H[: self.degree + 1], dim=-1)
        return (H_stack * self.coeffs).sum(-1)


class TropicalPoly(_ActivationBase):
    def __init__(
        self,
        degree: int,
        dim: Union[Sequence[int], int] = -1,
        keepdim: bool = False,
        requires_grad: bool = True,
    ):
        super().__init__()
        self.degree = degree
        self.a = nn.Parameter(torch.ones(degree + 1), requires_grad=requires_grad)
        self.keep_dim = keepdim
        self.dim = dim
        self.reset_parameters()

    def forward(self, x: Tensor):
        k = torch.arange(self.degree + 1, device=x.device, dtype=x.dtype)
        xk = x.unsqueeze(-1) * k  # broadcast over degree
        return torch.amax(self.a * xk, dim=self.dim)


class Fourier(_ActivationBase):
    def __init__(self, max_freq: int, requires_grad: bool = True):
        super().__init__()
        self.max_freq = max_freq
        self.a_sin = nn.Parameter(torch.ones(max_freq), requires_grad=requires_grad)
        self.a_cos = nn.Parameter(torch.ones(max_freq), requires_grad=requires_grad)
        self.reset_parameters()

    def forward(self, x):
        k = torch.arange(1, self.max_freq + 1, device=x.device, dtype=x.dtype)
        # Expand x: (..., 1) to broadcast with k: (max_freq,)
        xk = x.unsqueeze(-1) * k
        sin_terms = torch.sin(xk) * self.a_sin
        cos_terms = torch.cos(xk) * self.a_cos
        # Sum over frequencies
        return sin_terms.sum(-1) + cos_terms.sum(-1)


class HermiteSum(Hermite):
    def forward(self, x: Tensor):
        return x + super().forward(x)


class HermiteMul(Hermite):
    def forward(self, x: Tensor):
        return x * super().forward(x)


class TropicalPolySum(TropicalPoly):
    def forward(self, x: Tensor):
        return x + super().forward(x)


class TropicalPolyMul(TropicalPoly):
    def forward(self, x: Tensor):
        return x * super().forward(x)


class FourierSum(Fourier):
    def forward(self, x: Tensor):
        return x + super().forward(x)


class FourierMul(Fourier):
    def forward(self, x: Tensor):
        return x * super().forward(x)
