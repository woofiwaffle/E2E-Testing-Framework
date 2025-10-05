import yaml
from pathlib import Path

def get_config(path: str = "config/test_config.yaml") -> dict:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Config file not found: {path}")
    with p.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)
