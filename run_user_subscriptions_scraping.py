from src.requests.subscriptions_requester import SubscriptionsRequester
from src.mongo.driver import MongoDriver

FIELDS = ['name', 'is_closed', 'deactivated', 'is_member', 'type', 'activity', 'age_limits', 'description', 'counters', 'is_favourite']


def get_unprocessed_users():
    communities_mongo_driver = MongoDriver('communities')
    topology_mongo_driver = MongoDriver('topology')
    visited = communities_mongo_driver.get_all_ids()
    all = topology_mongo_driver.get_all_ids()
    unprocessed = list(set(all).difference(set(visited)))
    return unprocessed


if __name__ == "__main__":
    subscription_requester = SubscriptionsRequester()
    communities_mongo_driver = MongoDriver('communities')
    queue = get_unprocessed_users()
    counter = 0
    while len(queue) > 0:
        user_id = queue.pop()
        user_communities = subscription_requester.get_subscriptions(user_id, FIELDS)
        communities_mongo_driver.insert({"_id": user_id, "communities": user_communities})
        counter += 1
        if counter > 200:
            break


