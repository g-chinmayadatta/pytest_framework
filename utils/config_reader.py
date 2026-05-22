import yaml
from pathlib import Path

_CONFIG_PATH = Path(__file__).parent.parent / "config" / "config.yaml"
_USERS_PATH = Path(__file__).parent.parent / "test_data" / "users.yaml"

class ConfigReader:
    @staticmethod
    def load_config():
        with open(_CONFIG_PATH, "r") as file:
            all_config = yaml.safe_load(file)
        return all_config

    @staticmethod
    def load_api_config():
        with open(_CONFIG_PATH, "r") as file:
            return yaml.safe_load(file)

    @staticmethod
    def load_users():
        with open(_USERS_PATH, "r") as file:
            return yaml.safe_load(file)