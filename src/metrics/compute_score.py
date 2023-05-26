import torch

from src.metrics.metrics import Metrics
from src.metrics.compute_balanced_accuracy import compute_balanced_accuracy
from src.metrics.compute_columnwise_balanced_accuracy_score import compute_columnwise_balanced_accuracy
from src.metrics.compute_map_at_k import compute_map_at_k
    
def compute_score(y_true: torch.Tensor, y_pred: torch.Tensor, metric: Metrics) -> float:
    if metric == Metrics.balanced_accuracy:
        return compute_balanced_accuracy(y_true, y_pred)
    elif metric == Metrics.columnwise_balanced_accuracy:
        return compute_columnwise_balanced_accuracy(y_true, y_pred)
    elif metric == Metrics.map_at_k:
        return compute_map_at_k(y_true, y_pred)
    else:
        raise NotImplementedError()
