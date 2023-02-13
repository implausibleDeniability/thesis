import json
import requests

from rps_limiter import RpsLimiter


class FriendsRequester:
    url = "https://api.vk.com/method/friends.get"

    def __init__(self):
        with open("secrets.json") as file:
            secrets = json.load(file)
        self.access_token = secrets['access_token']
        self.rps_limiter = RpsLimiter()

    def get_friends(self, user_id: str) -> list[str]:
        self.rps_limiter.wait_till_next_available_request()
        params = {
            "user_id": user_id,
            "access_token": self.access_token,
            "v": "5.131",
        }
        response = requests.get(self.url, params=params).json()
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

