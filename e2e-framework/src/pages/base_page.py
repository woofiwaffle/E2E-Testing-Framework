from playwright.sync_api import Page
from src.utils.logger import get_logger

log = get_logger("BasePage")

class BasePage:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url

    def open(self, path: str = "/"):
        url = self.base_url.rstrip("/") + path
        log.info(f"Открываю страницу: {url}")
        self.page.goto(url)

    def click(self, selector: str):
        log.info(f"Клик по элементу: {selector}")
        self.page.wait_for_selector(selector)
        self.page.click(selector)

    def fill(self, selector: str, value: str):
        log.info(f"Заполняю {selector} значением '{value}'")
        self.page.wait_for_selector(selector)
        self.page.fill(selector, value)

    def text(self, selector: str) -> str:
        self.page.wait_for_selector(selector)
        return self.page.inner_text(selector)

    def is_visible(self, selector: str) -> bool:
        try:
            return self.page.is_visible(selector)
        except:
            return False
