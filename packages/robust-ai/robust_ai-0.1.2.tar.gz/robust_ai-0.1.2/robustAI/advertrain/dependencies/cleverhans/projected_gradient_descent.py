"""
Taken from https://github.com/rwightman/pytorch-image-models

The Projected Gradient Descent attack.

MIT License
"""
from typing import Optional

import numpy as np
import torch

from robustAI.advertrain.dependencies.cleverhans.fast_gradient_method import fast_gradient_method
from robustAI.advertrain.dependencies.cleverhans.utils import clip_eta


def projected_gradient_descent(
    model_fn,
    x: torch.Tensor,
    eps: float,
    eps_iter: float,
    nb_iter: int,
    norm: int,
    clip_min: Optional[float] = None,
    clip_max: Optional[float] = None,
    y: Optional[torch.Tensor] = None,
    targeted: bool = False,
    rand_init: bool = True,
    rand_minmax: Optional[float] = None,
    sanity_checks: bool = True,
) -> torch.Tensor:
    """
    Performs the Projected Gradient Descent attack.

    Args:
        model_fn: A callable that takes an input tensor and returns the model logits.
        x (torch.Tensor): Input tensor.
        eps (float): Epsilon, the input variation parameter.
        eps_iter (float): Step size for each attack iteration.
        nb_iter (int): Number of attack iterations.
        norm (int): Order of the norm (np.inf, 1, or 2).
        clip_min (float, optional): Mininum value per input dimension.
        clip_max (float, optional): Maximum value per input dimension.
        y (torch.Tensor, optional): Labels or target labels for targeted attack.
        targeted (bool): Whether to perform a targeted attack or not.
        rand_init (bool): Whether to start from a randomly perturbed input.
        rand_minmax (float, optional): Range of the uniform distribution for initial random perturbation.
        sanity_checks (bool): If True, include sanity checks.

    Returns:
        torch.Tensor: A tensor containing the adversarial examples.
    """
    if norm == 1:
        raise NotImplementedError(
            "It's not clear that FGM is a good inner loop"
            " step for PGD when norm=1, because norm=1 FGM "
            " changes only one pixel at a time. We need "
            " to rigorously test a strong norm=1 PGD "
            "before enabling this feature."
        )
    if norm not in [np.inf, 2]:
        raise ValueError("Norm order must be either np.inf or 2.")
    if eps < 0:
        raise ValueError(f"eps must be non-negative, got {eps}")
    if eps_iter < 0 or eps_iter > eps:
        raise ValueError(f"eps_iter must be in the range [0, {eps}], got {eps_iter}")

    if clip_min is not None and clip_max is not None and clip_min > clip_max:
        raise ValueError(f"clip_min must be less or equal to clip_max, got clip_min={clip_min}, clip_max={clip_max}")

    if sanity_checks:
        assert x.min() >= clip_min if clip_min is not None else True
        assert x.max() <= clip_max if clip_max is not None else True

    eta = (
        torch.zeros_like(x).uniform_(-rand_minmax if rand_minmax else eps, rand_minmax if rand_minmax else eps)
        if rand_init
        else torch.zeros_like(x)
    )

    # Clip eta and prepare adv_x
    eta = clip_eta(eta, norm, eps)
    adv_x = torch.clamp(x + eta, clip_min, clip_max) if clip_min is not None or clip_max is not None else x + eta

    y = torch.argmax(model_fn(x), dim=1) if y is None else y

    for _ in range(nb_iter):
        adv_x = fast_gradient_method(model_fn, adv_x, eps_iter, norm, clip_min, clip_max, y, targeted)
        eta = clip_eta(adv_x - x, norm, eps)
        adv_x = x + eta
        adv_x = torch.clamp(adv_x, clip_min, clip_max) if clip_min is not None or clip_max is not None else adv_x

    return adv_x
