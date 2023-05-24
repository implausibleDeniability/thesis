import numpy as np
import torch
from sklearn.metrics import balanced_accuracy_score

def compute_columnwise_balanced_accuracy(y_true: torch.Tensor, y_pred: torch.Tensor) -> float:
    accuracies = []
    for col_idx in range(y_true.shape[1]):
        accuracy = balanced_accuracy_score(
            y_true[:, col_idx] > 0.5, 
            y_pred[:, col_idx] > 0.5,
        )
        accuracies.append(accuracy)
    return np.mean(accuracies)

