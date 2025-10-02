"""
Taken from https://github.com/yaodongyu/TRADES

MIT License
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.autograd import Variable


def squared_l2_norm(x: torch.Tensor) -> torch.Tensor:
    """
    Compute the squared L2 norm of a tensor.

    Args:
        x (torch.Tensor): The input tensor.

    Returns:
        torch.Tensor: The squared L2 norm of the flattened input tensor.
    """
    flattened = x.view(x.unsqueeze(0).shape[0], -1)
    return (flattened ** 2).sum(1)


def l2_norm(x: torch.Tensor) -> torch.Tensor:
    """
    Compute the L2 norm of a tensor.

    Args:
        x (torch.Tensor): The input tensor.

    Returns:
        torch.Tensor: The L2 norm of the input tensor.
    """
    return squared_l2_norm(x).sqrt()


def trades_loss(
    model: nn.Module,
    x_natural: torch.Tensor,
    y: torch.Tensor,
    optimizer: torch.optim.Optimizer,
    step_size: float = 0.003,
    epsilon: float = 0.031,
    perturb_steps: int = 10,
    beta: float = 1.0,
    distance: str = "l_inf",
    device: torch.device = None
) -> torch.Tensor:
    """
    Calculate the TRADES loss for training robust models.

    Args:
        model (nn.Module): The neural network model.
        x_natural (torch.Tensor): Natural (clean) inputs.
        y (torch.Tensor): Target outputs.
        optimizer (torch.optim.Optimizer): Optimizer for the model.
        step_size (float, optional): Step size for perturbation. Defaults to 0.003.
        epsilon (float, optional): Perturbation limit. Defaults to 0.031.
        perturb_steps (int, optional): Number of perturbation steps. Defaults to 10.
        beta (float, optional): Regularization parameter for TRADES. Defaults to 1.0.
        distance (str, optional): Norm for perturbation ('l_inf' or 'l_2'). Defaults to 'l_inf'.
        device (torch.device, optional): The device to use (e.g., 'cuda' or 'cpu').

    Returns:
        torch.Tensor: The TRADES loss.
    """
    # define KL-loss
    criterion_kl = nn.KLDivLoss(size_average=False)
    model.eval()
    batch_size = len(x_natural)
    # generate adversarial example
    if "cuda" in str(device):
        x_adv = x_natural.detach() + 0.001 * torch.randn(x_natural.shape).cuda(device).detach()
    else:
        x_adv = x_natural.detach() + 0.001 * torch.randn(x_natural.shape).detach()
    if distance == "l_inf":
        for _ in range(perturb_steps):
            x_adv.requires_grad_()
            with torch.enable_grad():
                loss_kl = criterion_kl(
                    F.log_softmax(model(x_adv), dim=1),
                    F.softmax(model(x_natural), dim=1),
                )
            grad = torch.autograd.grad(loss_kl, [x_adv])[0]
            x_adv = x_adv.detach() + step_size * torch.sign(grad.detach())
            x_adv = torch.min(
                torch.max(x_adv, x_natural - epsilon), x_natural + epsilon
            )
            x_adv = torch.clamp(x_adv, 0.0, 1.0)
    elif distance == "l_2":
        if "cuda" in str(device):
            delta = 0.001 * torch.randn(x_natural.shape).cuda(device).detach()
        else:
            delta = 0.001 * torch.randn(x_natural.shape).detach()
        delta = Variable(delta.data, requires_grad=True)

        # Setup optimizers
        optimizer_delta = optim.SGD([delta], lr=epsilon / perturb_steps * 2)

        for _ in range(perturb_steps):
            adv = x_natural + delta

            # optimize
            optimizer_delta.zero_grad()
            with torch.enable_grad():
                loss = (-1) * criterion_kl(
                    F.log_softmax(model(adv), dim=1), F.softmax(model(x_natural), dim=1)
                )
            loss.backward()
            # renorming gradient
            grad_norms = delta.grad.view(batch_size, -1).norm(p=2, dim=1)
            delta.grad.div_(grad_norms.view(-1, 1, 1, 1))
            # avoid nan or inf if gradient is 0
            if (grad_norms == 0).any():
                delta.grad[grad_norms == 0] = torch.randn_like(
                    delta.grad[grad_norms == 0]
                )
            optimizer_delta.step()

            # projection
            delta.data.add_(x_natural)
            delta.data.clamp_(0, 1).sub_(x_natural)
            delta.data.renorm_(p=2, dim=0, maxnorm=epsilon)
        x_adv = Variable(x_natural + delta, requires_grad=False)
    else:
        x_adv = torch.clamp(x_adv, 0.0, 1.0)
    model.train()

    x_adv = Variable(torch.clamp(x_adv, 0.0, 1.0), requires_grad=False)
    # zero gradient
    optimizer.zero_grad()
    # calculate robust loss
    logits = model(x_natural)
    loss_natural = F.cross_entropy(logits, y)
    loss_robust = (1.0 / batch_size) * criterion_kl(
        F.log_softmax(model(x_adv), dim=1), F.softmax(model(x_natural), dim=1)
    )
    loss = loss_natural + beta * loss_robust
    return loss
