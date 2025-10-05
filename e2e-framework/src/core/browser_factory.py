from playwright.sync_api import sync_playwright
from src.utils.config_reader import get_config

def open_page():
    """Минимальная функция для открытия браузера"""
    cfg = get_config()
    pw = sync_playwright().start()
    
    browser = getattr(pw, cfg.get("browser", "chromium")).launch(
        headless=cfg.get("headless", True)
    )
    
    page = browser.new_page()
    page.set_default_timeout(cfg.get("timeouts", {}).get("default", 10000))
    
    return pw, browser, page