import math
import torch

from torch import nn, Tensor
from .basic_utils import _ActivationBase
from typing import Union, Sequence, Callable, Literal
from torch.nn import functional as F


class Hermite(_ActivationBase):
    def __init__(
        self,
        degree: int = 3,
        requires_grad: bool = True,
        version: Literal["original", "fast"] = "original",
    ):
        super().__init__()
        assert version in [
            "original",
            "fast",
        ], f"Invalid version '{version}'. It must be either 'original' or 'fast'"
        self.version = version
        degree = int(degree)
        assert (
            degree >= 1
        ), f"degree must be equal or larger than 1, received instead: {degree}"
        self.degree = degree
        # Learnable coefficients for each polynomial degree
        self.coeffs = nn.Parameter(
            torch.ones(degree + 1) * 1e-3, requires_grad=requires_grad
        )
        self.step_ld = 1.0 / (math.sqrt(degree) * math.pi)

    def _forward_ori(self, x: Tensor):
        H = [torch.ones_like(x), 2 * x]  # H0 and H1

        for n in range(2, self.degree + 1):
            Hn = 2 * x * H[-1] - 2 * (n - 1) * H[-2]
            H.append(Hn * self.step_ld)
        H_stack = torch.stack(H[: self.degree + 1], dim=-1)
        return (H_stack * self.coeffs).sum(-1)

    def _forward_fst(self, x: Tensor):
        h0, h1 = torch.ones_like(x), 2 * x
        if self.degree == 1:
            return h0 * self.coeffs[0] + h1 * self.coeffs[1]
        out = h0 * self.coeffs[0] + h1 * self.coeffs[1]
        for n in range(2, self.degree + 1):
            h0, h1 = h1, 2 * x * h1 - 2 * (n - 1) * h0
            out = out + h1 * self.coeffs[n] * self.step_ld
        return out

    def forward(self, x: Tensor):
        if self.version == "original":
            return self._forward_ori(x)
        return self._forward_fst(x)


class TropicalPoly(_ActivationBase):
    def __init__(
        self,
        degree: int = 3,
        keepdim: bool = False,
        version: Literal["original", "fast"] = "original",
        dim: Union[Sequence[int], int] = -1,
        requires_grad: bool = True,
    ):
        super().__init__()
        # version 0 shows the best quality, but slower
        assert version in [
            "original",
            "fast",
        ], f"Invalid version '{version}'. It must be either 'original' or 'fast'"
        self.version = version
        self.degree = degree
        self.a = nn.Parameter(
            torch.ones(degree + 1) * 1e-3, requires_grad=requires_grad
        )
        self.keep_dim = keepdim
        self.dim = dim
        k = torch.arange(self.degree + 1, dtype=torch.float32)
        self.register_buffer("k", k, True)
        self.reset_parameters()

    def _forward_ori(self, x: Tensor):
        xk = x.unsqueeze(-1) * self.k
        return torch.amax(self.a * xk, dim=self.dim)

    def _forward_fst(self, x: Tensor):
        out = self.a[0]  # scalar bias
        for k in range(1, self.degree + 1):
            out = torch.maximum(out, self.a[k] + k * x)
        return out

    def forward(self, x: Tensor):
        if self.version == "original":
            return self._forward_ori(x)
        return self._forward_fst(x)


class Fourier(_ActivationBase):
    def __init__(
        self,
        max_freq: int = 3,
        requires_grad: bool = True,
        version: Literal["original", "fast"] = "original",
    ):
        super().__init__()
        assert version in [
            "original",
            "fast",
        ], f"Invalid version '{version}'. It must be either 'original' or 'fast'"
        self.version = version
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

    def _forward_fst(self, x: Tensor):
        xk = x.unsqueeze(-1) * self.k
        complex_set = torch.polar(torch.ones_like(xk), xk)  # complex repr: exp(i xk)
        # sin = imag, cos = real
        return torch.sum(
            complex_set.real * self.real_base + complex_set.imag * self.imag_base,
            dim=-1,
        )

    def _forward_ori(self, x: Tensor):
        xk = x.unsqueeze(-1) * self.k
        sin_terms = torch.sin(xk) * self.a_sin
        cos_terms = torch.cos(xk) * self.a_cos
        # Sum over frequencies
        return torch.sum(sin_terms + cos_terms, dim=-1)

    def forward(self, x: Tensor):
        if self.version == "original":
            return self._forward_ori(x)
        return self._forward_fst(x)


class HermiteSum(Hermite):
    def forward(self, x: Tensor):
        return x + super().forward(x)


class HermiteMul(Hermite):
    def __init__(
        self,
        degree: int = 3,
        requires_grad: bool = True,
        norm_fn: Callable[[Tensor], Tensor] = F.tanh,
        version: Literal["original", "fast"] = "original",
    ):
        super().__init__(degree=degree, requires_grad=requires_grad, version=version)
        self.fc = norm_fn

    def forward(self, x: Tensor):
        return x * (1.0 + self.fc(super().forward(x)))


class TropicalPolySum(TropicalPoly):
    def forward(self, x: Tensor):
        return x + super().forward(x)


class TropicalPolyMul(TropicalPoly):
    def __init__(
        self,
        degree: int = 3,
        dim: Union[Sequence[int], int] = -1,
        keepdim: bool = False,
        requires_grad: bool = True,
        norm_fc: Callable[[Tensor], Tensor] = F.tanh,
        version: Literal["original", "fast"] = "original",
    ):
        super().__init__(
            degree=degree,
            dim=dim,
            keepdim=keepdim,
            requires_grad=requires_grad,
            version=version,
        )
        self.norm_fc = norm_fc

    def forward(self, x: Tensor):
        return x * (1 + self.norm_fc(super().forward(x)))


class FourierSum(Fourier):
    def forward(self, x: Tensor):
        return x + super().forward(x)


class FourierMul(Fourier):
    def __init__(
        self,
        max_freq: int = 3,
        requires_grad: bool = True,
        norm_fn: Callable[[Tensor], Tensor] = F.tanh,
        version: Literal["original", "fast"] = "original",
    ):
        super().__init__(
            max_freq=max_freq, requires_grad=requires_grad, version=version
        )
        self.norm_fc = norm_fn

    def forward(self, x: Tensor):
        return x * (1.0 + self.norm_fc(super().forward(x)))
