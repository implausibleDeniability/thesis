from typing import Callable


class BfsId:
    visited = set()
    queue = []

    def __init__(self, id: int, get_neighbors: Callable):
        self.queue.append(id)
        self.get_neighbors = get_neighbors

    def next(self) -> (int, list[int]):
        id = self.queue.pop(0)
        neighbouring_ids = self.get_neighbors(id)
        self._update_queue_with_new_nodes(neighbouring_ids)
        return id, neighbouring_ids

    def _update_queue_with_new_nodes(self, nodes: list[int]):
        new_ids = set(nodes) - self.visited
        self.queue.extend(list(new_ids))
