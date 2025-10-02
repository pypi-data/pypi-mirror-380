"""
Taken from https://github.com/rwightman/pytorch-image-models

The Fast Gradient Method attack.

MIT License
"""
from typing import Optional

import numpy as np
import torch

from robustAI.advertrain.dependencies.cleverhans.utils import optimize_linear


def fast_gradient_method(
    model_fn,
    x: torch.Tensor,
    eps: float,
    norm: int,
    clip_min: Optional[float] = None,
    clip_max: Optional[float] = None,
    y: Optional[torch.Tensor] = None,
    targeted: bool = False,
    sanity_checks: bool = False,
) -> torch.Tensor:
    """
    PyTorch implementation of the Fast Gradient Method (FGM).

    Args:
        model_fn: A callable that takes an input tensor and returns the model logits.
        x (torch.Tensor): Input tensor.
        eps (float): Epsilon, the input variation parameter.
        norm (int): Order of the norm (np.inf, 1, or 2).
        clip_min (float, optional): Mininum value per input dimension.
        clip_max (float, optional): Maximum value per input dimension.
        y (torch.Tensor, optional): Labels or target labels for targeted attack.
        targeted (bool): Whether to perform a targeted attack or not.
        sanity_checks (bool): If True, include sanity checks.

    Returns:
        torch.Tensor: A tensor containing the adversarial examples.
    """
    # Clipping perturbations
    if eps < 0:
        raise ValueError(f"eps must be greater than or equal to 0, got {eps} instead")
    if eps == 0:
        return x
    if clip_min is not None and clip_max is not None and clip_min > clip_max:
        raise ValueError(
            f"clip_min must be less than or equal to clip_max,got clip_min={clip_min},clip_max={clip_max}.")

    asserts = []

    # If a data range was specified,
    if clip_min is not None:
        assert_ge = torch.all(
            torch.ge(x, torch.tensor(clip_min, device=x.device, dtype=x.dtype))
        )
        asserts.append(assert_ge)

    if clip_max is not None:
        assert_le = torch.all(
            torch.le(x, torch.tensor(clip_max, device=x.device, dtype=x.dtype))
        )
        asserts.append(assert_le)

    if sanity_checks:
        assert np.all(asserts)
    # Prepare input tensor
    x = x.clone().detach().float().requires_grad_(True)
    y = torch.argmax(model_fn(x), dim=1) if y is None else y

    # Compute loss
    loss_fn = torch.nn.CrossEntropyLoss()
    loss = loss_fn(model_fn(x), y) * (-1 if targeted else 1)
    loss.backward()
    optimal_perturbation = optimize_linear(x.grad, eps, norm)

    # Optimize linear
    optimal_perturbation = optimize_linear(x.grad, eps, norm)
    adv_x = x + optimal_perturbation

    # Clipping perturbations
    if (clip_min is not None) or (clip_max is not None):
        if clip_min is None or clip_max is None:
            raise ValueError(
                "One of clip_min and clip_max is None but we don't currently support one-sided clipping"
            )
        adv_x = torch.clamp(adv_x, clip_min, clip_max)
    return adv_x
