import torch
from sklearn.metrics import balanced_accuracy_score

def compute_balanced_accuracy(y_true: torch.Tensor, y_pred: torch.Tensor) -> float:
    return balanced_accuracy_score(
        y_true.reshape(-1) > 0.5, 
        y_pred.reshape(-1) > 0.5,
    )
