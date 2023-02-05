from api import Api
from bfs import BfsId
from mongo_driver import MongoDriver


if __name__ == "__main__":
    api = Api()
    my_id = 35084928
    get_neighbors = api.get_friends
    bfs = BfsId(my_id, get_neighbors)
    mongo_driver = MongoDriver()
    while True:
        user, friends = bfs.next()
        mongo_driver.insert({"_id": user, "friends": friends})

