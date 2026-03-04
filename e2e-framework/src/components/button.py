from src.pages.base_page import BasePage

class Button(BasePage):
    def click(self, selector: str):
        super().click(selector)