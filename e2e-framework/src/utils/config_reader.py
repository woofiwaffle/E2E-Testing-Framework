import os
import yaml
import logging
from pathlib import Path

log = logging.getLogger(__name__)

DEFAULT_CONFIG = "demoapp.local.yaml"
CONFIG_DIR = Path("config")

def get_config(config_name: str | None = None) -> dict:
    if config_name:
        filename = config_name
    else:
        filename = os.getenv("TEST_CONFIG", DEFAULT_CONFIG)

    path = CONFIG_DIR / filename

    if not path.exists():
        log.error("Configuration file not found: %s", path)
        raise FileNotFoundError(f"Config file not found: {path}")

    with path.open("r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    log.info("Loaded config: %s", path)
    return config