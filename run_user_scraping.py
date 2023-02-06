from api import Api
from bfs import Bfs
from bfs_loader import BfsBuilder
from mongo_driver import MongoDriver


if __name__ == "__main__":
    api = Api()
    users_mongo_driver = MongoDriver('users')
    topology_mongo_driver = MongoDriver('topology')
    visited = users_mongo_driver.get_all_ids()
    queue = topology_mongo_driver.get_all_ids()
    queue = list(set(queue).difference(set(visited)))
    while True:
        queue = mongo_driver
    bfs = BfsBuilder(mongo_driver).build(get_neighbors)
    while True:
        user, friends = bfs.next()
        mongo_driver.insert({"_id": user, "friends": friends})

