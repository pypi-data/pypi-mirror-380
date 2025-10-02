import json
import os
from typing import Any, Dict

import torch
from torch import Tensor

from robustAI.advertrain.constants import METRICS_FILE


class Metrics:
    """
    Class to track performance metrics for binary classification tasks.

    This class tracks true positives, true negatives, false positives,
    false negatives, and cumulative loss across batches. It calculates metrics
    like accuracy, precision, recall, and F1-score.
    """

    def __init__(self):
        self.reset_metrics()

    def reset_metrics(self) -> None:
        """Reset all metrics to zero."""
        self.loss = 0
        self.TP = self.TN = self.FP = self.FN = self.P = self.N = 0

    def update(self, x: Tensor, y: Tensor, pred: Tensor, loss: Tensor) -> None:
        """
        Update metrics based on inputs, ground truth, model predictions, and loss.

        Args:
            x (Tensor): Input tensor
            y (Tensor): target labels
            pred (Tensor): Model predictions
            loss (Tensor): Batch loss
        """
        TP = torch.logical_and(pred == 1, y == 1)
        TN = torch.logical_and(pred == 0, y == 0)
        FP = torch.logical_and(pred == 1, y == 0)
        FN = torch.logical_and(pred == 0, y == 1)

        self.P += torch.sum(y == 1)
        self.N += torch.sum(y == 0)

        self.TP += torch.sum(TP)
        self.TN += torch.sum(TN)
        self.FP += torch.sum(FP)
        self.FN += torch.sum(FN)

        self.loss += loss.item() * len(x)

    def _precision(self) -> float:
        return self.TP / (self.TP + self.FP + 1e-8)

    def _recall(self) -> float:
        return self.TP / (self.P + 1e-8)

    def _f1_score(self) -> float:
        precision = self._precision()
        recall = self._recall()
        return 2 * precision * recall / (precision + recall + 1e-8)

    def get_metrics(self) -> tuple:
        """
        Calculate and return key performance metrics.

        Returns:
            tuple: Tuple containing accuracy, loss, precision, recall, and F1-score.
        """
        acc = (self.TP + self.TN) / (self.P + self.N + 1e-8)
        loss = self.loss / (self.P + self.N + 1e-8)
        precision = self._precision()
        recall = self._recall()
        f1_score = self._f1_score()

        return acc, loss, precision, recall, f1_score

    def save_metrics(self, metrics: Dict[str, Any], checkpoint: str) -> None:
        """
        Save metrics in a JSON file located at `<checkpoint>/metrics.json`.

        This function serializes the provided metrics dictionary into JSON format and
        writes it to a file named 'metrics.json' in the specified checkpoint directory.

        Args:
            metrics (Dict[str, Any]): A dictionary containing metric names as keys and their corresponding values.
            checkpoint (str): The directory path where the metrics.json file will be saved.
        """
        data = json.dumps(metrics)
        with open(os.path.join(checkpoint, METRICS_FILE), "w", encoding="utf-8") as f:
            f.write(data)

    def load_metrics(self, checkpoint: str) -> Dict[str, Any]:
        """
        Load metrics from a JSON file located at `<checkpoint>/metrics.json`.

        This function reads the 'metrics.json' file from the specified checkpoint directory
        and returns the contents as a dictionary.

        Args:
            checkpoint (str): The directory path from where the metrics.json file will be loaded.

        Returns:
            Dict[str, Any]: A dictionary containing the loaded metrics.
        """
        with open(os.path.join(checkpoint, METRICS_FILE), "r", encoding="utf-8") as file:
            data = json.load(file)

        return data

    def display(self, title: str) -> None:
        """
        Display the calculated metrics with a title.

        Args:
            title (str): The title for the metrics display.
        """
        acc, loss, precision, recall, f1_score = self.get_metrics()
        print(f"{title}\n"
              f"Loss: {loss:.3f}\t"
              f"Acc: {acc:.3f}\t"
              f"Recall: {recall:.3f}\t"
              f"Precision: {precision:.3f}\t"
              f"F1 Score: {f1_score:.3f}")

    def display_table(self, title: str) -> None:
        """
        Display the metrics in a tabular format with a title.

        Args:
            title (str): The title for the table.
        """
        acc, loss, precision, recall, f1_score = self.get_metrics()
        print(f"| {title} | {acc:.3f} |{loss:.3f} | {recall:.3f} | {precision:.3f} | {f1_score:.3f} |")
