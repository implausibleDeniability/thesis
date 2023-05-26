import torch
from src.metrics import Metrics


def compute_loss(y_true: torch.Tensor, y_pred: torch.Tensor, loss_type: Metrics):
    elementwise_loss = torch.nn.functional.binary_cross_entropy(y_pred, y_true, reduction='none')
    assert len(elementwise_loss.shape) == 2
    with torch.no_grad():
        if loss_type == Metrics.columnwise_balanced_accuracy:
            positive_to_negative_ratio = y_true.mean(axis=0) / (1 - y_true.mean(axis=0))
            positive_coefficients = (y_true > 0.5) / positive_to_negative_ratio
            negative_coefficients = (y_true < 0.5) #* positive_to_negative_ratio
            coefficients = positive_coefficients + negative_coefficients
        elif loss_type == Metrics.balanced_accuracy:
            positive_to_negative_ratio = y_true.mean() / (1 - y_true.mean())
            positive_coefficients = (y_true > 0.5) / positive_to_negative_ratio
            negative_coefficients = (y_true < 0.5) #* positive_to_negative_ratio
            coefficients = positive_coefficients + negative_coefficients
        else:
            raise NotImplementedError()
    balanced_loss = elementwise_loss * coefficients
    loss = balanced_loss.mean()
    return loss
