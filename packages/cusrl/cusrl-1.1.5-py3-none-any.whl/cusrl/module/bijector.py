import math
from typing import TypeVar

import torch
from torch import Tensor, nn

__all__ = [
    "Bijector",
    "ExponentialBijector",
    "IdentityBijector",
    "SigmoidBijector",
    "SoftplusBijector",
    "make_bijector",
]

FloatOrTensor = TypeVar("FloatOrTensor", float, Tensor)


class Bijector(nn.Module):
    """Abstract base class for bijective transformations.

    A bijector represents an invertible function. This class provides an
    interface for such transformations. Subclasses should implement both the
    `forward` and `inverse` methods.

    Methods:
        forward(input):
            Computes the forward transformation, :math:`f(x)`.
        inverse(input):
            Computes the inverse transformation, :math:`f^{-1}(y)`.
    """

    def forward(self, input: FloatOrTensor) -> FloatOrTensor:
        raise NotImplementedError

    def inverse(self, input: FloatOrTensor) -> FloatOrTensor:
        raise NotImplementedError


class ExponentialBijector(Bijector):
    def __init__(self, min_value: float = 0.01, max_value: float = 1.0):
        super().__init__()
        self.min_value, self.max_value = min_value, max_value
        self.min_input = self.inverse(min_value)
        self.max_input = self.inverse(max_value)

    def forward(self, input: FloatOrTensor) -> FloatOrTensor:
        if isinstance(input, Tensor):
            return torch.exp(input.clamp(self.min_input, self.max_input))
        return math.exp(min(max(input, self.min_input), self.max_input))

    def inverse(self, input: FloatOrTensor) -> FloatOrTensor:
        if isinstance(input, Tensor):
            return torch.log(input.clamp(self.min_value, self.max_value))
        return math.log(min(max(input, self.min_value), self.max_value))

    def extra_repr(self):
        return f"min={self.min_value}, max={self.max_value}"


class IdentityBijector(Bijector):
    def forward(self, input: FloatOrTensor) -> FloatOrTensor:
        return input

    def inverse(self, input: FloatOrTensor) -> FloatOrTensor:
        return input


class SigmoidBijector(Bijector):
    def __init__(self, min_value: float = 0.0, max_value: float = 1.0, eps: float = 0.01):
        super().__init__()
        self.min_value = min_value
        self.max_value = max_value
        self.range = max_value - min_value
        self.eps = eps

    def forward(self, input: FloatOrTensor) -> FloatOrTensor:
        if isinstance(input, Tensor):
            return self.min_value + self.range * torch.sigmoid(input)
        return self.min_value + self.range * (1 / (1 + math.exp(-input)))

    def inverse(self, input: FloatOrTensor) -> FloatOrTensor:
        if isinstance(input, Tensor):
            clamped_input = input.clamp(self.min_value + self.eps, self.max_value - self.eps)
            return torch.log((clamped_input - self.min_value) / (self.max_value - clamped_input))
        clamped_input = max(self.min_value + self.eps, min(input, self.max_value - self.eps))
        return math.log((clamped_input - self.min_value) / (self.max_value - clamped_input))

    def extra_repr(self):
        return f"min={self.min_value}, max={self.max_value}, eps={self.eps}"


class SoftplusBijector(Bijector):
    def __init__(self, scale: float = 1.0, min_value: float = 0.01, max_value: float = 1.0):
        super().__init__()
        self.scale = scale
        self.min_value, self.max_value = min_value, max_value
        self.min_input = self.inverse(min_value)
        self.max_input = self.inverse(max_value)

    def forward(self, input: FloatOrTensor) -> FloatOrTensor:
        if isinstance(input, Tensor):
            clamped_input = input.clamp(self.min_input, self.max_input)
            return torch.nn.functional.softplus(clamped_input * self.scale) / self.scale
        clamped_input = max(self.min_input, min(input, self.max_input))
        return math.log1p(math.exp(clamped_input * self.scale)) / self.scale

    def inverse(self, input: FloatOrTensor) -> FloatOrTensor:
        if isinstance(input, Tensor):
            clamped_input = input.clamp(self.min_value, self.max_value)
            return torch.log(torch.expm1(clamped_input * self.scale)) / self.scale
        clamped_input = max(self.min_value, min(input, self.max_value))
        return math.log(math.expm1(clamped_input * self.scale)) / self.scale

    def extra_repr(self):
        return f"scale={self.scale}, min={self.min_value}, max={self.max_value}"


def make_bijector(bijector: str | Bijector | None) -> Bijector:
    if isinstance(bijector, Bijector):
        return bijector
    if bijector is None:
        return IdentityBijector()
    bijector_type, *params = bijector.split("_")
    bijector_type = bijector_type.lower()
    params = [float(param) for param in params]
    if not bijector_type or bijector_type == "identity":
        return IdentityBijector(*params)
    if bijector_type == "exp" or bijector_type == "exponential":
        return ExponentialBijector(*params)
    if bijector_type == "sigmoid":
        return SigmoidBijector(*params)
    if bijector_type == "softplus":
        return SoftplusBijector(*params)
    raise ValueError(f"Unknown bijector '{bijector}'.")
