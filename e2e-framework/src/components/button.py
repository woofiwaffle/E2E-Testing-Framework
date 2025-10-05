from src.pages.base_page import BasePage

class Button(BasePage):
    """
    Компонент кнопки.
    Используется внутри страниц.
    """
    def click(self, selector: str):
        self.page.wait_for_selector(selector)
        self.page.click(selector)