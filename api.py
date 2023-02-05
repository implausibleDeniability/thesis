import json

import requests


class Api:
    def __init__(self):
        with open("secrets.json") as file:
            secrets = json.load(file)
        self.access_token = secrets['access_token']

    def get_friends(self, user_id: str) -> list[str]:
        url = "https://api.vk.com/method/friends.get"
        params = {
            "user_id": user_id,
            "access_token": self.access_token,
            "v": "5.131",
        }
        response = requests.get(url, params=params)
        friend_ids = response.json()['response']['items']
        return friend_ids

