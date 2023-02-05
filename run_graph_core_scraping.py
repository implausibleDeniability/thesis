from api import Api
from bfs import BfsId


if __name__ == "__main__":
    api = Api()
    my_id = 35084928
    get_neighbors = api.get_friends
    bfs = BfsId(my_id, get_neighbors)
    while True:
        user, friends = bfs.next()

