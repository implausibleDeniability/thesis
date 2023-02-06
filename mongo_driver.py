from typing import Iterable
from pymongo import MongoClient


class MongoDriver:
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.graph_topology = self.client['graph-vk']['core']

    def insert(self, data: dict):
        self.graph_topology.insert_one(data)

    def get_all_documents(self) -> Iterable[dict]:
        return self.graph_topology.find({})

    def get_all_ids(self) -> Iterable[int]:
        ids = [int(id) for id in self.graph_topology.distinct("_id")]
        return ids

