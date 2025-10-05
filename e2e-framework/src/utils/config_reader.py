import yaml
from pathlib import Path

def get_config(path: str = "config/test_config.yaml") -> dict:
    """Чтение конфига с значениями по умолчанию"""
    p = Path(path)
    if not p.exists():
        return {
            "browser": "chromium",
            "headless": True,
            "timeouts": {"default": 10000}
        }
    
    with p.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)