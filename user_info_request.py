import json
import requests

from rps_limiter import RpsLimiter


class InfoRequester:
    url = "https://api.vk.com/method/users.get"

    def __init__(self):
        with open("secrets.json") as file:
            secrets = json.load(file)
        self.access_token = secrets['access_token']
        self.rps_limiter = RpsLimiter()

    def get_single_user_info(self, user_id: int, fields: list[str]) -> dict:
        self.rps_limiter.wait_till_next_available_request()
        params = {
            "user_id": user_id,
            "access_token": self.access_token,
            "v": "5.131",
            "fields": ", ".join(fields),
        }
        response = requests.get(self.url, params=params).json()['response'][0]
        return response

    def get_many_users_info(self, user_ids: list[int], fields: list[str]) -> list[dict]:
        self.rps_limiter.wait_till_next_available_request()
        params = {
            "user_id": ",".join(list(map(str, user_ids))),
            "access_token": self.access_token,
            "v": "5.131",
            "fields": "sex,bdate,city,country,university,faculty,graduation,personal",
        }
        response = requests.get(self.url, params=params)
        data = response.json()['response']
        return data

