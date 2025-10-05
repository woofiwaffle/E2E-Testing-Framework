import pytest
from src.utils.config_reader import get_config

@pytest.fixture(scope="session")
def config():
    """Базовая фикстура конфига"""
    return get_config()
