import os
import yaml
from dotenv import load_dotenv

load_dotenv()


class Config:
    @property
    def appium_url(self):
        host = os.getenv("APPIUM_HOST", "127.0.0.1")
        port = os.getenv("APPIUM_PORT", "4723")
        return f"http://{host}:{port}"

    @property
    def device_caps(self):
        profile = os.getenv("DEVICE_PROFILE", "emulator")
        config_path = os.path.join(os.path.dirname(__file__), "device_config.yaml")
        with open(config_path, "r") as f:
            all_caps = yaml.safe_load(f)
        return all_caps[profile]

    @property
    def app_path(self):
        return os.getenv("APP_PATH")
