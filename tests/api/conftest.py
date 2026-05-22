from src.api.api_client import APIClient
from src.api.api_endpoint import Endpoints
from utils.config_reader import ConfigReader
import pytest


@pytest.fixture
def api_client():

    config = ConfigReader.load_api_config()
    base_url = config["api_url"]

    return APIClient(base_url)


@pytest.fixture
def book_cleanup(api_client):
    created_ids = []

    def register(book_id):
        created_ids.append(book_id)

    yield register

    for book_id in created_ids:
        try:
            api_client.delete(Endpoints.DELETE_BOOK, json={"ID": book_id})
        except Exception:
            pass