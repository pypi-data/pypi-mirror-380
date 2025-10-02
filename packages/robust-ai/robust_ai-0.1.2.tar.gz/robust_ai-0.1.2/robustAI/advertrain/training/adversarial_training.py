from typing import Tuple

import numpy as np
import torch
from torch import Tensor
from torch.nn import Module
from torch.optim import Optimizer

from robustAI.advertrain.dependencies.cleverhans.projected_gradient_descent import \
    projected_gradient_descent
from robustAI.advertrain.training.classical_training import ClassicalTraining


class AdversarialTraining(ClassicalTraining):
    """
    A training class that incorporates adversarial training using Projected Gradient Descent (PGD).

    This class extends ClassicalTraining by modifying the preprocessing of batches to include
    the generation of adversarial examples using PGD.

    Attributes:
        epsilon (float): The maximum perturbation allowed for adversarial examples.
    """

    def __init__(
        self,
        model: Module,
        optimizer: Optimizer,
        loss_func,
        device: torch.device,
        epsilon: float,
    ) -> None:
        """
        Initializes the AdversarialTraining class.

        Args:
            model (Module): The neural network model to be trained.
            optimizer (Optimizer): The optimizer for training the model.
            loss_func: The loss function to be used for training.
            device (torch.device): The device for training.
            epsilon (float): The maximum perturbation allowed for adversarial examples.
        """
        self.epsilon = epsilon
        super().__init__(model, optimizer, loss_func, device)

    def preprocess_batch(
        self, x: Tensor, y: Tensor, epoch: int
    ) -> Tuple[Tensor, Tensor]:
        """
        Preprocesses a batch of data by generating adversarial examples using PGD.

        Args:
            x (Tensor): The input data batch.
            y (Tensor): The ground truth labels batch.
            epoch (int): The current training epoch.

        Returns:
            Tuple[Tensor, Tensor]: A tuple of adversarial examples and their corresponding labels.
        """
        n_steps = 20

        adv_x = projected_gradient_descent(
            model_fn=self.model,
            x=x,
            eps=self.epsilon,
            eps_iter=self.epsilon / n_steps,
            nb_iter=n_steps,
            norm=np.inf,
            clip_min=0,
            clip_max=1,
            sanity_checks=False,
        )

        return adv_x, y
