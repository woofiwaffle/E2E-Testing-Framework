from src.pages.base_page import BasePage
from src.components.button import Button
from src.components.input import Input

class ExamplePage(BasePage):
    """
    Пример страницы, которая использует компоненты.
    """
    HEADER = "h1"
    BUTTON_DEMO = "button#demo"
    INPUT_DEMO = "input#demo"

    def __init__(self, page, base_url):
        super().__init__(page, base_url)
        self.button = Button(page, base_url)
        self.input = Input(page, base_url)

    def open_home(self):
        self.open("/")
        self.page.wait_for_load_state("networkidle")

    def header_text(self) -> str:
        if self.is_visible(self.HEADER):
            return self.text(self.HEADER)
        return ""

    def fill_demo_input(self, value: str):
        self.input.fill(self.INPUT_DEMO, value)

    def click_demo_button(self):
        self.button.click(self.BUTTON_DEMO)