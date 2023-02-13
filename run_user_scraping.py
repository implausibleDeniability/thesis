from src.requests.info_requester import InfoRequester
from src.mongo_driver import MongoDriver

REQUEST_BATCH_SIZE = 100
FIELDS = ['sex', 'bdate', 'city', 'country', 'university', 'faculty', 'graduation', 'personal']


def get_unprocessed_users():
    users_mongo_driver = MongoDriver('users')
    topology_mongo_driver = MongoDriver('topology')
    visited = users_mongo_driver.get_all_ids()
    all = topology_mongo_driver.get_all_ids()
    unprocessed = list(set(all).difference(set(visited)))
    return unprocessed


if __name__ == "__main__":
    info_requester = InfoRequester()
    users_mongo_driver = MongoDriver('users')
    queue = get_unprocessed_users()
    while len(queue) > 0:
        batch_user_ids = queue[:REQUEST_BATCH_SIZE]
        queue = queue[REQUEST_BATCH_SIZE:]
        batch_users_data = info_requester.get_many_users_info(batch_user_ids, FIELDS)
        for user_id, user_data in zip(batch_user_ids, batch_users_data):
            users_mongo_driver.insert({"_id": user_id, **user_data})

