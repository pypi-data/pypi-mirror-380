from torch import Tensor, nn
from .basic_utils import _ActivationBase
from lt_utils.common import *
from torch.nn import functional as F


class ScaleMinMax(_ActivationBase):
    def __init__(
        self,
        min_value: Optional[Number] = None,
        max_value: Optional[Number] = None,
        eps: float = 1e-7,
        dim: Optional[Union[int, Sequence[int]]] = None,
    ):
        super().__init__()
        self.min_value = min_value
        self.max_value = max_value
        self.eps = eps
        self.dim = dim

    def forward(self, x: Tensor) -> Tensor:
        if self.min_value is None and self.max_value is None:
            return x
        if self.dim is None:
            x_min, x_max = x.amin(), x.amax()
        else:
            x_min, x_max = x.amin(dim=self.dim), x.amax(dim=self.dim)

        min_val = x_min if self.min_value is None else self.min_value
        max_val = x_max if self.max_value is None else self.max_value
        return (x - x_min) / (x_max - x_min + self.eps) * (max_val - min_val) + min_val


class SoftCELU(_ActivationBase):
    def __init__(self, alpha=1.0):
        super().__init__()
        self.celu = nn.CELU(alpha=alpha)

    def forward(self, x):
        return F.softplus(x) * self.celu(x)
