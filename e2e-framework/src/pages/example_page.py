import time
from src.pages.base_page import BasePage
from src.components.button import Button
from src.components.input import Input

class ExamplePage(BasePage):
    HEADER = "h1"
    INPUT_DEMO = "input#demo-input"
    BUTTON_DEMO = "button#demo-button"
    RESULT = "#result"

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

    def get_result_text(self) -> str:
        """Возвращает текущий текст в #result (немедленно)."""
        self.page.wait_for_selector(self.RESULT)
        return self.page.inner_text(self.RESULT)

    def wait_for_result_text(self, expected: str, timeout: int = 10000) -> str:
        end = time.time() + (timeout / 1000.0)
        last_text = ""
        while time.time() < end:
            try:
                el = self.page.query_selector(self.RESULT)
                if el:
                    last_text = el.inner_text()
                    if expected in last_text:
                        return last_text
            except Exception:
                # если DOM ещё не готов — проигнорируем и попробуем снова
                pass
            time.sleep(0.1)
        # по таймауту — вернуть текущее содержимое (для логов) и упасть в тесте
        try:
            return last_text or self.get_result_text()
        except Exception:
            raise RuntimeError(f"Timed out waiting for result text to contain '{expected}' (timeout={timeout}ms)")

