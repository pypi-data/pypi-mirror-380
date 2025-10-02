"""
Taken from https://github.com/rwightman/pytorch-image-models

MIT License
"""
import numpy as np
import torch


def clip_eta(eta: torch.Tensor, norm: int, eps: float) -> torch.Tensor:
    """
    Clips the perturbation eta to be within the specified norm ball.

    Args:
        eta (torch.Tensor): The perturbation tensor.
        norm (int): The norm to use.
        eps (float): Epsilon, the maximum allowed norm of the perturbation.

    Returns:
        torch.Tensor: The clipped perturbation.
    """
    if norm not in [np.inf, 1, 2]:
        raise ValueError("Norm must be np.inf, 1, or 2.")

    elif norm == np.inf:
        eta = torch.clamp(eta, -eps, eps)
    else:
        avoid_zero_div = torch.tensor(1e-12, dtype=eta.dtype, device=eta.device)
        reduc_ind = list(range(1, len(eta.size())))
        norm_val = (
            torch.sqrt(torch.sum(eta**2, dim=reduc_ind, keepdim=True))
            if norm == 2
            else torch.sum(torch.abs(eta), dim=reduc_ind, keepdim=True)
        )
        norm_val = torch.max(norm_val, avoid_zero_div)
        factor = torch.min(torch.tensor(1.0, dtype=eta.dtype, device=eta.device), eps / norm_val)
        eta *= factor

    return eta


def optimize_linear(grad: torch.Tensor, eps: float, norm: int = np.inf) -> torch.Tensor:
    """
    Solves for the optimal input to a linear function under a norm constraint.

    Args:
        grad (torch.Tensor): Tensor of gradients.
        eps (float): Epsilon, the maximum allowed norm of the perturbation.
        norm (int): The norm to use.

    Returns:
        torch.Tensor: The optimized perturbation.
    """
    red_ind = list(range(1, len(grad.size())))
    avoid_zero_div = torch.tensor(1e-12, dtype=grad.dtype, device=grad.device)

    if norm == np.inf:
        optimal_perturbation = torch.sign(grad)
    elif norm == 1:
        abs_grad = torch.abs(grad)
        sign = torch.sign(grad)
        red_ind = list(range(1, len(grad.size())))
        abs_grad = torch.abs(grad)
        ori_shape = [1] * len(grad.size())
        ori_shape[0] = grad.size(0)

        max_abs_grad, _ = torch.max(abs_grad.view(grad.size(0), -1), 1)
        max_mask = abs_grad.eq(max_abs_grad.view(ori_shape)).to(torch.float)
        num_ties = max_mask
        for red_scalar in red_ind:
            num_ties = torch.sum(num_ties, red_scalar, keepdim=True)
        optimal_perturbation = sign * max_mask / num_ties
        opt_pert_norm = optimal_perturbation.abs().sum(dim=red_ind)
        assert torch.all(opt_pert_norm == torch.ones_like(opt_pert_norm))
    elif norm == 2:
        square = torch.max(avoid_zero_div, torch.sum(grad ** 2, red_ind, keepdim=True))
        optimal_perturbation = grad / torch.sqrt(square)

        opt_pert_norm = (
            optimal_perturbation.pow(2).sum(dim=red_ind, keepdim=True).sqrt()
        )
        one_mask = (square <= avoid_zero_div).to(torch.float) * opt_pert_norm + (
            square > avoid_zero_div
        ).to(torch.float)
        assert torch.allclose(opt_pert_norm, one_mask, rtol=1e-05, atol=1e-08)
    else:
        raise ValueError("Only L-inf, L1 and L2 norms are currently implemented.")

    scaled_perturbation = eps * optimal_perturbation
    return scaled_perturbation
