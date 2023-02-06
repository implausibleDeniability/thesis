from api import Api
from bfs import Bfs
from bfs_builder import BfsBuilder
from mongo_driver import MongoDriver


if __name__ == "__main__":
    api = Api()
    get_neighbors = api.get_friends
    mongo_driver = MongoDriver()
#     my_id = 395182538
#     bfs = Bfs(my_id, get_neighbors)
    bfs = BfsBuilder(mongo_driver).build(get_neighbors)
    while True:
        user, friends = bfs.next()
        mongo_driver.insert({"_id": user, "friends": friends})

