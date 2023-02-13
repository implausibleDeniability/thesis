from bfs_builder import BfsBuilder
from mongo_driver import MongoDriver
from user_friends_request import FriendsRequester


if __name__ == "__main__":
    friends_requester = FriendsRequester()
    get_neighbors = friends_requester.get_friends
    mongo_driver = MongoDriver('topology')
#     my_id = 395182538
#     bfs = Bfs(my_id, get_neighbors)
    bfs = BfsBuilder(mongo_driver).build(get_neighbors)
    while True:
        user, friends = bfs.next()
        mongo_driver.insert({"_id": user, "friends": friends})

