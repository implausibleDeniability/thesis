from typing import Callable
from bfs import Bfs
from mongo_driver import MongoDriver


class BfsBuilder:
    def __init__(self, mongo_driver: MongoDriver):
        self.mongo_driver = mongo_driver

    def build(self, get_neighbors: Callable) -> Bfs:
        visited = set(self.mongo_driver.get_all_ids())
        queue = set()
        for node in self.mongo_driver.get_all_documents():
            queue.update(node['friends'])
        queue = list(queue.difference(visited))
        bfs = Bfs(None, get_neighbors)
        bfs.load_state(queue, visited)
        return bfs
        
        
