import json
from pymongo import MongoClient
from src.mongo import configs as mongo_config


class MongoDumper:
    def __init__(self):
        client = MongoClient(mongo_config.DBMS_IP, mongo_config.DBMS_PORT)
        self.database = client[mongo_config.DATABASE_NAME]
        self.collection_names = self.database.list_collection_names()

    def dump(self, path: str="mongo_dump.json") -> None:
        data = {}
        for collection_name in self.collection_names:
            collection_data = self.database[collection_name].find({})
            data[collection_name] = list(collection_data)
        self._save_dict_on_disk(data, path)

    def _save_dict_on_disk(self, dict_: dict, path: str) -> None:
        with open(path, 'w') as file:
            json.dump(dict_, file)


