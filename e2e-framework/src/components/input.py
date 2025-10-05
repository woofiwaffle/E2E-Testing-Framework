from src.pages.base_page import BasePage

class Input(BasePage):
    """
    Компонент текстового поля.
    """
    def fill(self, selector: str, value: str):
        self.page.wait_for_selector(selector)
        self.page.fill(selector, value)