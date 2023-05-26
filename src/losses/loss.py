import torch

from src.metrics import Metrics
from src.losses.compute_loss import compute_loss

class Loss:
    def __init__(self, loss_type: Metrics):
        self.loss_type = loss_type

    def __call__(self, y_true: torch.Tensor, y_pred: torch.Tensor):
        return compute_loss(y_true, y_pred, self.loss_type)
