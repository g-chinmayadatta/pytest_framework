from src.api.api_client import APIClient
from src.util.config_reader import ConfigReader
import pytest


@pytest.fixture
def api_client():

    config = ConfigReader.load_api_config()
    base_url = config["api_url"]

    return APIClient(base_url)