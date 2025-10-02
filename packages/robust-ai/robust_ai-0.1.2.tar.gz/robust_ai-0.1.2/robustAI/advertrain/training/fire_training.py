import torch

from robustAI.advertrain.dependencies.fire import fire_loss
from robustAI.advertrain.training.classical_training import ClassicalTraining


class FIRETraining(ClassicalTraining):
    def __init__(
        self,
        model: torch.nn.Module,
        optimizer: torch.optim.Optimizer,
        device: torch.device,
        epsilon: float,
        beta: float,
        perturb_steps: int = 20
    ):
        """
        Initialize the FIRETraining class for adversarial and robust training of neural network models.

        This class extends ClassicalTraining by incorporating the FIRE (Fast and Improved Robustness Estimation) loss
        in the training process, which is designed for adversarial training scenarios.

        Args:
            model (torch.nn.Module): The neural network model to be trained.
            optimizer (torch.optim.Optimizer): The optimizer used for training.
            device (torch.device): The device on which to perform calculations.
            epsilon (float): Perturbation size for adversarial example generation.
            beta (float): Weight for the robust loss in the overall loss calculation.
            perturb_steps (int, optional): Number of steps for adversarial example generation (Defaults to 20).
        """
        super().__init__(model, optimizer, None, device)

        self.epsilon = epsilon
        self.beta = beta
        self.perturb_steps = perturb_steps
        self.step_size = epsilon / perturb_steps

    def train_batch(self, x: torch.Tensor, y: torch.Tensor, epoch: int) -> tuple[float, int]:
        """
        Train the model for one batch of data.

        Args:
            x (torch.Tensor): The input data.
            y (torch.Tensor): The labels corresponding to the input data.
            epoch (int): The current epoch number.

        Returns:
            tuple[float, int]: A tuple containing the loss value and the batch size.
        """
        x, y = x.to(self.device), y.to(self.device)
        x, y = self.preprocess_batch(x, y, epoch)
        x = x.clamp(0, 1)

        self.optimizer.zero_grad()
        loss, a, b, c = fire_loss(
            self.model,
            x,
            y,
            self.optimizer,
            epoch,
            self.device,
            step_size=self.step_size,
            epsilon=self.epsilon,
            perturb_steps=self.perturb_steps,
            beta=self.beta,
        )

        loss.backward()
        self.optimizer.step()

        output = self.model(x)
        pred = torch.argmax(output, dim=1)

        self.metrics.update(x, y, pred, loss)

        return (
            loss.item(),
            len(x),
        )

    def val_batch(self, x: torch.Tensor, y: torch.Tensor, epoch: int) -> tuple[float, int]:
        """
        Validate the model for one batch of data.

        Args:
            x (torch.Tensor): The input data.
            y (torch.Tensor): The labels corresponding to the input data.
            epoch (int): The current epoch number.

        Returns:
            tuple[float, int]: A tuple containing the loss value and the batch size.
        """
        x, y = x.to(self.device), y.to(self.device)

        with torch.no_grad():
            loss, _, _, _ = fire_loss(
                self.model,
                x,
                y,
                self.optimizer,
                epoch,
                self.device,
                step_size=self.step_size,
                epsilon=self.epsilon,
                perturb_steps=self.perturb_steps,
                beta=self.beta,
            )

            output = self.model(x)
            pred = torch.argmax(output, dim=1)

            self.metrics.update(x, y, pred, loss)

        return (
            loss.item(),
            len(x),
        )
