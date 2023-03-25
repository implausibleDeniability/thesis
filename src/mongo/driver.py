from typing import Iterable
from pymongo import MongoClient


class MongoDriver:
    def __init__(self, collection_name: str):
        self.client = MongoClient('localhost', 27017)
        self.collection = self.client['graph-vk'][collection_name]

    def insert(self, data: dict):
        self.collection.insert_one(data)

    def get_all_documents(self) -> Iterable[dict]:
        return self.collection.find({})

    def get_all_ids(self) -> Iterable[int]:
        ids = [int(id) for id in self.collection.distinct("_id")]
        return ids

