import math
import torch

from torch import nn, Tensor
from .basic_utils import _ActivationBase
from typing import Union, Sequence, Callable
from torch.nn import functional as F


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
        degree: int = 3,
        keepdim: bool = False,
        requires_grad: bool = True,
    ):
        super().__init__()
        self.degree = degree
        self.a = nn.Parameter(torch.ones(degree + 1), requires_grad=requires_grad)
        self.keep_dim = keepdim
        self.reset_parameters()

    def forward(self, x: Tensor):
        out = self.a[0]  # scalar bias
        for k in range(1, self.degree + 1):
            out = torch.maximum(out, self.a[k] + k * x)
        return out


class Fourier(_ActivationBase):
    def __init__(self, max_freq: int = 3, requires_grad: bool = True):
        super().__init__()
        self.max_freq = max_freq
        self.imag_base = nn.Parameter(
            torch.ones(max_freq, dtype=torch.float32), requires_grad=requires_grad
        )
        self.real_base = nn.Parameter(
            torch.ones(max_freq, dtype=torch.float32), requires_grad=requires_grad
        )
        k = torch.arange(1, self.max_freq + 1, dtype=torch.float32)
        self.register_buffer("k", k)
        self.reset_parameters()

    def forward(self, x):
        xk = x.unsqueeze(-1) * self.k
        complex_set = torch.polar(torch.ones_like(xk), xk)  # complex repr: exp(i xk)
        # sin = imag, cos = real
        return torch.sum(
            complex_set.real * self.real_base + complex_set.imag * self.imag_base,
            dim=-1,
        )


class HermiteSum(Hermite):
    def forward(self, x: Tensor):
        return x + super().forward(x)


class HermiteMul(Hermite):
    def __init__(
        self,
        degree: int,
        requires_grad: bool = True,
        gated_activ: Callable[[Tensor], Tensor] = F.tanh,
    ):
        super().__init__(degree, requires_grad)
        self.fc = gated_activ

    def forward(self, x: Tensor):
        return x * (1.0 + self.fc(super().forward(x)))


class TropicalPolySum(TropicalPoly):
    def forward(self, x: Tensor):
        return x + super().forward(x)


class TropicalPolyMul(TropicalPoly):
    def __init__(
        self,
        degree: int,
        dim: Union[Sequence[int], int] = -1,
        keepdim: bool = False,
        requires_grad: bool = True,
        gated_activ: Callable[[Tensor], Tensor] = F.tanh,
    ):
        super().__init__(degree, dim, keepdim, requires_grad)
        self.fc = gated_activ

    def forward(self, x: Tensor):
        return x * (1 + self.fc(super().forward(x)))


class FourierSum(Fourier):
    def forward(self, x: Tensor):
        return x + super().forward(x)


class FourierMul(Fourier):
    def __init__(
        self,
        max_freq: int,
        requires_grad: bool = True,
        gated_activ: Callable[[Tensor], Tensor] = F.tanh,
    ):
        super().__init__(max_freq, requires_grad)
        self.fc = gated_activ

    def forward(self, x: Tensor):
        return x * (1.0 + self.fc(super().forward(x)))
