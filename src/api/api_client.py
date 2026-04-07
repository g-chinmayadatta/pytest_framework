import requests
from src.api.api_logger import APILogger


class APIClient:

    def __init__(self, base_url):
        self.base_url = base_url

    def post(self, endpoint, json=None):
        url = f"{self.base_url}{endpoint}"
        APILogger.log_request("POST", url, payload=json)

        response = requests.post(url, json=json)

        APILogger.log_response(response)
        return response

    def get(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"
        APILogger.log_request("GET", url, params=params)

        response = requests.get(url, params=params)

        APILogger.log_response(response)
        return response

    def delete(self, endpoint, json=None):
        url = f"{self.base_url}{endpoint}"
        APILogger.log_request("POST", url, payload=json)

        response = requests.post(url, json=json)

        APILogger.log_response(response)
        return response