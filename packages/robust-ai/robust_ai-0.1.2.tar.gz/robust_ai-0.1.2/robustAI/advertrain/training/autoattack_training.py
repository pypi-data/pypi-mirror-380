"""
This module contains the class for ClassicalTraining including aversarial training using AutoGPD attack
"""
from typing import Callable, Tuple

import torch
from robustAI.advertrain.dependencies.autoattack import APGDAttack
from robustAI.advertrain.training.classical_training import ClassicalTraining


class AutoAttackTraining(ClassicalTraining):
    """
    Extends ClassicalTraining to include adversarial training using AutoPGD attacks.

    Attributes:
        epsilon (float): The maximum perturbation amount allowed for the APGD attack.
        apgd_loss (str): The loss function to be used in the APGD attack.
        apgd (APGDAttack): Instance of APGDAttack for generating adversarial examples.

    Methods:
        preprocess_batch(x, y, epoch): Processes each batch by generating adversarial examples.
    """
    def __init__(
        self,
        model: torch.nn.Module,
        optimizer: torch.optim.Optimizer,
        loss_func: Callable,
        device: torch.device,
        loss: str,
        epsilon: float
    ):
        """
        Initializes the AutoAttackTraining object with the given parameters.

        Args:
            model (torch.nn.Module): The neural network model to be trained.
            optimizer (torch.optim.Optimizer): The optimizer used for training.
            loss_func (Callable): The loss function used for training.
            device (torch.device): The device on which to perform computations.
            loss (str): The type of loss function to use in the APGD attack.
            epsilon (float): The maximum perturbation amount allowed for the APGD attack.
        """
        super().__init__(model, optimizer, loss_func, device)

        self.epsilon = epsilon
        self.apgd_loss = loss
        self.apgd = APGDAttack(
            self.model, eps=self.epsilon, loss=self.apgd_loss, device=self.device
        )

    def preprocess_batch(self, x: torch.Tensor, y: torch.Tensor, epoch: int) -> Tuple[torch.Tensor, torch.Tensor]:
        """
        Processes each batch by generating adversarial examples.

        Args:
            x (torch.Tensor): Input data (images).
            y (torch.Tensor): Corresponding labels.
            epoch (int): The current epoch number.

        Returns:
            Tuple[torch.Tensor, torch.Tensor]: A tuple containing the adversarial examples and their corresponding
            labels.
        """
        adv_x = self.apgd.perturb(x, y)
        return adv_x, y
