"""
Taken from https://github.com/MarinePICOT/Adversarial-Robustness-via-Fisher-Rao-Regularization

Robust training losses. Based on code from
https://github.com/MarinePICOT/Adversarial-Robustness-via-Fisher-Rao-Regularization/blob/main/src/losses.py
"""

import numpy as np
import torch
import torch.nn.functional as F
from torch.autograd import Variable


def entropy_loss(unlabeled_logits: torch.Tensor) -> torch.Tensor:
    """
    Calculate the entropy loss for a batch of unlabeled data.

    Args:
        unlabeled_logits (torch.Tensor): A tensor of logits from a model's output.
        It should have a shape of (batch_size, num_classes).

    Returns:
        torch.Tensor: The mean entropy loss across the batch.
    """
    unlabeled_probs = torch.nn.functional.softmax(unlabeled_logits, dim=1)
    return (
        -(unlabeled_probs * torch.nn.functional.log_softmax(unlabeled_logits, dim=1))
        .sum(dim=1)
        .mean(dim=0)
    )


def fire_loss(
    model: torch.nn.Module,
    x_natural: torch.Tensor,
    y: torch.Tensor,
    optimizer: torch.optim.Optimizer,
    epoch: int,
    device: torch.device,
    step_size: float = 0.003,
    epsilon: float = 0.001,
    perturb_steps: int = 10,
    beta: float = 1.0,
    adversarial: bool = True,
    distance: str = "Linf",
    entropy_weight: float = 0,
    pretrain: int = 0,
) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
    """
    This function calculates the FIRE (Fast and Improved Robustness Estimation) loss,
    which is a combination of natural loss, robust loss, and entropy loss for unlabeled data.
    It is used for adversarial training and stability training of neural networks.

    Args:
        model (torch.nn.Module): The neural network model to be trained.
        x_natural (torch.Tensor): Input tensor of natural (non-adversarial) images.
        y (torch.Tensor): Tensor of labels. Unlabeled data should have label -1.
        optimizer (torch.optim.Optimizer): The optimizer used for training.
        epoch (int): Current training epoch.
        device (torch.device): The device on which to perform calculations.
        step_size (float): Step size for adversarial example generation.
        epsilon (float): Perturbation size for adversarial example generation.
        perturb_steps (int): Number of steps for adversarial example generation.
        beta (float): Weight for the robust loss in the overall loss calculation.
        adversarial (bool): Flag to enable/disable adversarial training.
        distance (str): Type of distance metric for adversarial example generation ("Linf" or "L2").
        entropy_weight (float): Weight for the entropy loss in the overall loss calculation.
        pretrain (int): Number of pretraining epochs.

    Returns:
        tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]: A tuple containing
        the total loss, natural loss, robust loss, and entropy loss for unlabeled data.
    """

    if beta == 0:
        logits = model(x_natural)
        loss = F.cross_entropy(logits, y)
        inf = torch.Tensor([np.inf])
        zero = torch.Tensor([0.0])
        return loss, loss, inf, zero

    is_unlabeled = y == -1
    if epoch < pretrain:
        logits = model(x_natural)
        loss = F.cross_entropy(logits, y)
        loss_natural = loss
        loss_robust = torch.Tensor([0.0])
        if torch.sum(is_unlabeled) > 0:
            logits_unlabeled = logits[is_unlabeled]
            loss_entropy_unlabeled = entropy_loss(logits_unlabeled)
            loss = loss + entropy_weight * loss_entropy_unlabeled
        else:
            loss_entropy_unlabeled = torch.tensor(0)

    else:
        model.eval()  # moving to eval mode to freeze batchnorm stats
        # batch_size = len(x_natural)
        # generate adversarial example
        x_adv = x_natural.detach() + 0.0  # the + 0. is for copying the tensor
        s_nat = model(x_natural).softmax(1).detach()
        if adversarial:
            if distance == "Linf":
                x_adv += 0.001 * torch.randn(x_natural.shape).to(device)

                for _ in range(perturb_steps):
                    x_adv.requires_grad_()
                    with torch.enable_grad():
                        s_adv = model(x_adv).softmax(1)
                        sqroot_prod = ((s_nat * s_adv) ** 0.5).sum(1)
                        # In line below, Minus eps to prevent gradient
                        # explosion near 1 (https://github.com/pytorch/pytorch/issues/8069)
                        loss_kl = (torch.acos(sqroot_prod - 1e-7) ** 2).mean(0)

                    grad = torch.autograd.grad(loss_kl, [x_adv])[0]
                    x_adv = x_adv.detach() + step_size * torch.sign(grad.detach())
                    x_adv = torch.min(
                        torch.max(x_adv, x_natural - epsilon), x_natural + epsilon
                    )
                    x_adv = torch.clamp(x_adv, 0.0, 1.0)
            else:
                raise ValueError(f"No support for distance {distance} in adversarial training")
        else:
            if distance == "L2":
                x_adv = x_adv + epsilon * torch.randn_like(x_adv)
            else:
                raise ValueError(f"No support for distance {distance} in stability training")

        model.train()  # moving to train mode to update batchnorm stats

        # zero gradient
        optimizer.zero_grad()

        x_adv = Variable(torch.clamp(x_adv, 0.0, 1.0), requires_grad=False)
        logits_nat = model(x_natural)
        logits_adv = model(x_adv)

        s_adv = logits_adv.softmax(1)
        s_nat = logits_nat.softmax(1)

        loss_natural = F.cross_entropy(logits_nat, y, ignore_index=-1)

        sqroot_prod = ((s_nat * s_adv) ** 0.5).sum(1)
        # In line below, Minus eps to prevent gradient explosion near 1 (https://github.com/pytorch/pytorch/issues/8069)
        loss_robust = (torch.acos(sqroot_prod - 1e-7) ** 2).mean(0)

        loss = loss_natural + beta * loss_robust

        if torch.sum(is_unlabeled) > 0:
            logits_unlabeled = logits[is_unlabeled]
            loss_entropy_unlabeled = entropy_loss(logits_unlabeled)
            loss = loss + entropy_weight * loss_entropy_unlabeled
        else:
            loss_entropy_unlabeled = torch.tensor(0)

    return loss, loss_natural, loss_robust, loss_entropy_unlabeled


def noise_loss(
    model: torch.nn.Module,
    x_natural: torch.Tensor,
    y: torch.Tensor,
    epsilon: float = 0.25,
    clamp_x: bool = True
) -> torch.Tensor:
    """
    This function augments the input data with random noise and computes the loss
    based on the model's predictions for the noisy data.
    Args:
        model (torch.nn.Module): The neural network model.
        x_natural (torch.Tensor): The original (clean) input data.
        y (torch.Tensor): The labels corresponding to the input data.
        epsilon (float, optional): The magnitude of the noise to be added to the input data.
          Defaults to 0.25.
        clamp_x (bool, optional): If True, the noisy data is clamped to the range [0.0, 1.0].
          Defaults to True.

    Returns:
        torch.Tensor: The computed loss based on the model's predictions for the noisy data.
    """
    x_noise = x_natural + epsilon * torch.randn_like(x_natural)
    if clamp_x:
        x_noise = x_noise.clamp(0.0, 1.0)
    logits_noise = model(x_noise)
    loss = F.cross_entropy(logits_noise, y, ignore_index=-1)
    return loss
