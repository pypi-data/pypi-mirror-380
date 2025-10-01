import os
import configparser

def get_app_version():
    config_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "config.properties"
    )
    config = configparser.ConfigParser()
    config.read(config_path)
    try:
        return config.get("APP VERSION", "APP_VERSION").strip('"').strip("'")
    except Exception:
        return "Unknown"