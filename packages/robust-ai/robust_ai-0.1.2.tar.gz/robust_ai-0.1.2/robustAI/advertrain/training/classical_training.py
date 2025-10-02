"""
This module contains the class for classic training process
"""

import os
from typing import Any, Dict, Tuple

import numpy as np
import torch
from torch.nn import Module
from torch.optim import Optimizer
from torch.utils.data import DataLoader
from tqdm import tqdm

from robustAI.advertrain.metrics import Metrics


class ClassicalTraining:
    """
    A class representing the classical training process for a PyTorch model.

    Attributes:
        model (Module): The PyTorch model to be trained.
        optimizer (Optimizer): The optimizer used for training.
        loss_func: The loss function used for training.
        device (torch.device): The device on which to train the model.
        metrics (Metrics): An instance of Metrics to track training performance.
    """

    def __init__(
        self, model: Module, optimizer: Optimizer, loss_func, device: torch.device
    ) -> None:
        self.model = model
        self.loss_func = loss_func
        self.device = device
        self.optimizer = optimizer
        self.metrics = Metrics()
        self.metrics.reset_metrics()

    def preprocess_batch(
        self, x: torch.Tensor, y: torch.Tensor, epoch: int
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        """
        Preprocess a batch of data and labels before training or validation.

        Args:
            x (torch.Tensor): Input data batch.
            y (torch.Tensor): Corresponding labels batch.
            epoch (int): The current epoch number.

        Returns:
            Tuple[torch.Tensor, torch.Tensor]: The preprocessed data and labels.
        """
        return x, y

    def train_batch(
        self, x: torch.Tensor, y: torch.Tensor, epoch: int
    ) -> Tuple[float, int]:
        """
        Process and train a single batch of data.

        Args:
            x (torch.Tensor): Input data batch.
            y (torch.Tensor): Corresponding labels batch.
            epoch (int): The current epoch number.

        Returns:
            Tuple[float, int]: The training loss for the batch and the batch size.
        """
        x, y = self._to_device(x, y)
        x.clamp_(0, 1)

        self.optimizer.zero_grad()
        output = self.model(x)
        loss = self.loss_func(output, y)
        loss.backward()
        self.optimizer.step()

        pred = torch.argmax(output, dim=1)
        self.metrics.update(x, y, pred, loss)

        return loss.item(), len(x)

    def val_batch(
        self, x: torch.Tensor, y: torch.Tensor, epoch: int
    ) -> Tuple[float, int]:
        """
        Validate a single batch of data.

        Args:
            x (torch.Tensor): Input data batch.
            y (torch.Tensor): Corresponding labels batch.
            epoch (int): The current epoch number.

        Returns:
            Tuple[float, int]: The validation loss for the batch and the batch size.
        """
        x, y = self._to_device(x, y)

        with torch.no_grad():
            output = self.model(x)
            loss = self.loss_func(output, y)

        pred = torch.argmax(output, dim=1)
        self.metrics.update(x, y, pred, loss)

        return loss.item(), len(x)

    def fit(
        self,
        epochs: int,
        train_dataloader: DataLoader,
        val_dataloader: DataLoader,
        patience: int,
        checkpoint: str
    ) -> Dict[str, Any]:
        """
        Train and validate the model over a given number of epochs, implementing early stopping.

        Args:
            epochs (int): The total number of epochs to train.
            train_dataloader (DataLoader): The DataLoader for the training data.
            val_dataloader (DataLoader): The DataLoader for the validation data.
            patience (int): The number of epochs to wait for improvement before stopping early.
            checkpoint (str): Path to save the model checkpoints.

        Returns:
            Dict[str, Any]: A dictionary containing training and validation metrics.
        """
        wait = 0
        val_loss_min = np.Inf

        metrics = {
            "loss": [], "acc": [],
            "val_loss": [], "val_acc": [],
            "optimizer": str(self.optimizer),
            "loss_func": str(self.loss_func),
            "epochs": epochs, "patience": patience
        }

        for epoch in range(epochs):
            (
                train_acc,
                train_loss,
                train_precision_defect,
                train_recall_defect,
                train_f1_score_defect,
            ) = self._process_epoch(train_dataloader, epochs, epoch, train=True)
            (
                val_acc,
                val_loss,
                val_precision_defect,
                val_recall_defect,
                val_f1_score_defect,
            ) = self._process_epoch(val_dataloader, epochs, epoch, train=False)

            # update metrics
            metrics = self._update_metrics(metrics, train_loss.item(), train_acc.item(),
                                           val_loss.item(), val_acc.item()
                                           )

            print(
                f"Epoch {epoch + 1}/{epochs}\n"
                f"Train Loss: {train_loss:.3f}, Acc: {train_acc:.3f}, "
                f"Recall: {train_recall_defect:1.3f}, Precision: {train_precision_defect:1.3f}, "
                f"F1 Score: {train_f1_score_defect:.3f}\n"
                f"Validation Loss: {val_loss:.3f}, Acc: {val_acc:.3f}, "
                f"Recall: {val_recall_defect:1.3f}, Precision: {val_precision_defect:1.3f}, "
                f"F1 Score: {val_f1_score_defect:.3f}"
            )

            # Checkpoint
            self.metrics.save_metrics(metrics, checkpoint)

            if val_loss < val_loss_min:
                print(f"Validation loss decreased ({val_loss_min:.6f} --> {val_loss:.6f}). Saving model ...")
                torch.save(self.model.state_dict(), os.path.join(checkpoint, "model.pth"))
                val_loss_min = val_loss
                wait = 0

            # Early stopping
            else:
                wait += 1
                if wait > patience:
                    print(
                        f"Terminated training for early stopping at epoch {epoch + 1}"
                    )
                    break

        return metrics

    def _to_device(self, x: torch.Tensor, y: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        """Moves tensors to the specified device."""
        return x.to(self.device), y.to(self.device)

    def _process_epoch(self, dataloader: DataLoader, epochs: int, epoch: int, train: bool) -> Dict[str, float]:
        """
        Process a single epoch of training or validation.

        Args:
            dataloader (DataLoader): The DataLoader for the epoch.
            epoch (int): The current epoch number.
            train (bool): Flag indicating whether it's a training epoch.

        Returns:
            Dict[str, float]: Metrics for the processed epoch.
        """
        self.metrics.reset_metrics()
        if train:
            self.model.train()
            for x, y in tqdm(
                dataloader,
                desc=f"Epochs {epoch + 1}/{epochs} : Training",
                position=0,
                leave=True,
            ):
                self.train_batch(x, y, epoch)
        else:
            self.model.eval()
            for x, y in tqdm(
                dataloader,
                desc="Validation",
                position=0,
                leave=True,
            ):
                self.val_batch(x, y, epoch)

        return self.metrics.get_metrics()

    def _update_metrics(self, metrics: Dict[str, Any], train_loss: float, train_acc: float,
                        val_loss: float, val_acc: float) -> None:
        """
        Update the overall metrics dictionary with the metrics from the current epoch.

        Args:
            metrics (Dict[str, Any]): The overall metrics dictionary.
            train_metrics (Dict[str, float]): Metrics from the training phase.
            val_metrics (Dict[str, float]): Metrics from the validation phase.
        """
        metrics['loss'].append(train_loss)
        metrics['acc'].append(train_acc)
        metrics['val_loss'].append(val_loss)
        metrics['val_acc'].append(val_acc)

        return metrics
