import json
import time
import requests


class Api:
    TIME_BETWEEN_REQUESTS = 0.5
    get_friends_url = "https://api.vk.com/method/friends.get"

    def __init__(self):
        with open("secrets.json") as file:
            secrets = json.load(file)
        self.access_token = secrets['access_token']
        self.previous_request_time = 0

    def get_friends(self, user_id: str) -> list[str]:
        self._wait_minimal_rps()
        params = {
            "user_id": user_id,
            "access_token": self.access_token,
            "v": "5.131",
        }
        response = requests.get(self.get_friends_url, params=params).json()
        if "error" in response:
            if response['error']['error_code'] == 18:
                return [] # deleted profile
            elif response['error']['error_code'] == 30:
                return [] # private profile
            else:
                print(response)
        else:
            friend_ids = response['response']['items']
            return friend_ids

    def _wait_minimal_rps(self):
        time_to_wait = max(
            self.previous_request_time + self.TIME_BETWEEN_REQUESTS - time.time(),
            0,
        )
        self.previous_request_time = time.time()
        time.sleep(time_to_wait)

