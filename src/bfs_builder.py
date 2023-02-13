from typing import Callable, Iterable
from src.bfs import Bfs
from src.mongo_driver import MongoDriver


class BfsBuilder:
    MY_ID = 395182538

    def __init__(self, mongo_driver: MongoDriver):
        self.mongo_driver = mongo_driver

    def build(self, get_neighbors: Callable) -> Bfs:
        queue, visited = self.load_state_from_mongo()
        bfs = Bfs(self.MY_ID, get_neighbors)
        if len(visited) != 0:
            bfs.load_state(queue, visited)
        return bfs

    def load_state_from_mongo(self) -> (Iterable[int], Iterable[int]):
        visited = set(self.mongo_driver.get_all_ids())
        queue = set()
        for node in self.mongo_driver.get_all_documents():
            queue.update(node['friends'])
        queue = list(queue.difference(visited))
        return queue, visited

        
