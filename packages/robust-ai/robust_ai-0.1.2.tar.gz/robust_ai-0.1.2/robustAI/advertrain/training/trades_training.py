import torch
from torch.nn import Module

from robustAI.advertrain.dependencies.trades import trades_loss
from robustAI.advertrain.training.classical_training import ClassicalTraining


class TRADESTraining(ClassicalTraining):
    def __init__(
        self,
        model: Module,
        optimizer: torch.optim.Optimizer,
        device: torch.device,
        epsilon: float,
        beta: float,
        perturb_steps: int = 20,
    ):
        """
        Initialize the TRADES training procedure.

        Args:
            model (nn.Module): The neural network model.
            optimizer (torch.optim.Optimizer): Optimizer for the model.
            device (torch.device): The device to use for training (e.g., 'cuda' or 'cpu').
            epsilon (float): The perturbation limit.
            beta (float): The regularization parameter for TRADES.
            perturb_steps (int, optional): Number of perturbation steps. Defaults to 20.
        """
        super().__init__(model, optimizer, None, device)

        self.model = model
        self.device = device
        self.optimizer = optimizer
        self.epsilon = epsilon
        self.step_size = epsilon / perturb_steps
        self.perturb_steps = perturb_steps
        self.beta = beta

    def train_batch(self, x: torch.Tensor, y: torch.Tensor, epoch: int) -> tuple[float, int]:
        """
        Train the model on a batch of data.

        Args:
            x (torch.Tensor): Input data.
            y (torch.Tensor): Target labels.

        Returns:
            tuple[float, int]: Tuple containing the loss and the number of examples in the batch.
        """
        x, y = x.to(self.device), y.to(self.device)

        self.optimizer.zero_grad()
        loss = trades_loss(
            model=self.model,
            x_natural=x,
            y=y,
            optimizer=self.optimizer,
            step_size=self.step_size,
            epsilon=self.epsilon,
            perturb_steps=self.perturb_steps,
            beta=self.beta,
            distance="l_inf",
            device=self.device
        )

        output = self.model(x)
        pred = torch.argmax(output, dim=1)

        self.metrics.update(x, y, pred, loss)

        loss.backward()
        self.optimizer.step()

        return (
            loss.item(),
            len(x),
        )

    def val_batch(self, x: torch.Tensor, y: torch.Tensor, epoch: int) -> tuple[float, int]:
        """
        Validate the model on a batch of data.

        Args:
            x (torch.Tensor): Input data.
            y (torch.Tensor): Target labels.

        Returns:
            tuple[float, int]: Tuple containing the loss and the number of examples in the batch.
        """
        x, y = x.to(self.device), y.to(self.device)

        with torch.no_grad():
            loss = trades_loss(
                model=self.model,
                x_natural=x,
                y=y,
                optimizer=self.optimizer,
                step_size=self.step_size,
                epsilon=self.epsilon,
                perturb_steps=self.perturb_steps,
                beta=self.beta,
                distance="l_inf",
                device=self.device
            )

            output = self.model(x)
            pred = torch.argmax(output, dim=1)

            self.metrics.update(x, y, pred, loss)

        return (
            loss.item(),
            len(x),
        )
