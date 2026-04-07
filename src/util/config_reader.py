import yaml

class ConfigReader:
    @staticmethod
    def load_config(env_name=None):
        with open("config/config.yaml", "r") as file:
            all_config = yaml.safe_load(file)

        if env_name not in all_config:
            raise KeyError(f"Environment '{env_name}' not found in config.yaml!")

        return all_config[env_name]

    @staticmethod
    def load_api_config():
        with open("config/config.yaml", "r") as file:
            all_config = yaml.safe_load(file)
            return all_config