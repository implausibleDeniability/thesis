from enum import Enum

class Metrics(Enum):
    balanced_accuracy = 0
    columnwise_balanced_accuracy = 1
    map_at_k = 2

    @classmethod
    def from_string(cls, metric: str) -> Metrics:
        if metric == "balanced_accuracy":
            return cls.balanced_accuracy
        elif metric == "columnwise_balanced_accuracy":
            return cls.columnwise_balanced_accuracy
        elif metric == "map_at_k":
            return cls.map_at_k
        else:
            raise NotImplementedError()
