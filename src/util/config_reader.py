import yaml
from pathlib import Path

_CONFIG_PATH = Path(__file__).parent.parent.parent / "config" / "config.yaml"

class ConfigReader:
    @staticmethod
    def load_config(env_name=None):
        with open(_CONFIG_PATH, "r") as file:
            all_config = yaml.safe_load(file)

        if env_name not in all_config:
            raise KeyError(f"Environment '{env_name}' not found in config.yaml!")

        return all_config[env_name]

    @staticmethod
    def load_api_config():
        with open(_CONFIG_PATH, "r") as file:
            return yaml.safe_load(file)