import numpy as np
import torch


def compute_map_at_k(y_true, y_pred, k=5) -> float:
    precisions = []
    for user_true, user_pred in zip(y_true, y_pred):
        if user_true.sum() < 1.0:
            continue
        top_k_predicted = torch.argsort(user_pred, descending=True)[:k]
        max_k_predicted = min(k, user_true.sum())
        precision_at_k = user_true[top_k_predicted].sum() / max_k_predicted
        precisions.append(precision_at_k)
    return np.mean(precisions)
