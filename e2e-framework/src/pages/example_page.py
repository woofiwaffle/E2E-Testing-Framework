from src.pages.base_page import BasePage
from src.components.button import Button
from src.components.input import Input

class ExamplePage(BasePage):
    """
    Страница demo-app с компонентами.
    """
    HEADER = "h1"
    INPUT_DEMO = "input#demo-input"
    BUTTON_DEMO = "button#demo-button"

    def __init__(self, page, base_url):
        super().__init__(page, base_url)
        self.input = Input(page, base_url)
        self.button = Button(page, base_url)

    def open_home(self):
        self.open("/")
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_selector(self.HEADER)

    def header_text(self) -> str:
        return self.text(self.HEADER)

    def fill_demo_input(self, value: str):
        self.input.fill(self.INPUT_DEMO, value)

    def click_demo_button(self):
        self.button.click(self.BUTTON_DEMO)
