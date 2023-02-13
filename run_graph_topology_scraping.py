from src.bfs_builder import BfsBuilder
from src.mongo_driver import MongoDriver
from src.requests.friends_requester import FriendsRequester


if __name__ == "__main__":
    friends_requester = FriendsRequester()
    get_neighbors = friends_requester.get_friends
    mongo_driver = MongoDriver('topology')
    bfs = BfsBuilder(mongo_driver).build(get_neighbors)
    while True:
        user, friends = bfs.next()
        mongo_driver.insert({"_id": user, "friends": friends})

