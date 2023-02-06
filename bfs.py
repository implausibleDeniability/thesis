from typing import Callable, Iterable


class Bfs:
    visited = set()
    queue = []

    def __init__(self, id: int, get_neighbors: Callable):
        self.queue.append(id)
        self.visited.add(id)
        self.get_neighbors = get_neighbors

    def load_state(self, queue: Iterable[int], visited: Iterable[int]) -> None:
        self.queue = list(set(queue).difference(set(visited)))
        self.visited = set(visited)

    def next(self) -> (int, list[int]):
        id = self.queue.pop(0)
        neighbouring_ids = self.get_neighbors(id)
        self._update_queue_with_new_nodes(neighbouring_ids)
        return id, neighbouring_ids

    def _update_queue_with_new_nodes(self, nodes: list[int]):
        new_ids = set(nodes) - self.visited
        self.queue.extend(list(new_ids))
        self.visited.update(new_ids)
