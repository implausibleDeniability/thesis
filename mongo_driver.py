from pymongo import MongoClient


class MongoDriver:
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['graph-vk']['core']

    def insert(self, data: dict):
        self.db.insert_one(data)

