import logging
from playwright.sync_api import Page

log = logging.getLogger(__name__)

class BasePage:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url


    # ===== Navigation =====
    def open(self, path: str = "/"):
        url = self.base_url.rstrip("/") + path
        log.info("Open URL: %s", url)
        #self.page.goto(url)
        self.page.goto(url, wait_until="domcontentloaded")

    def reload(self):
        log.info("Reload page")
        self.page.reload()


    # ===== Actions =====
    def click(self, selector: str):
        self.page.wait_for_selector(selector)
        self.page.click(selector)
        log.info("Click element: %s", selector)

    def fill(self, selector: str, value: str):
        self.page.wait_for_selector(selector)
        self.page.fill(selector, value)
        log.info("Fill element: %s with value='%s'", selector, value)

    def press(self, selector: str, key: str = "Enter"):
        self.page.wait_for_selector(selector)
        self.page.press(selector, key)
        log.info("Press key '%s' on element: %s", key, selector)

    def set_input_files(self, selector: str, file_paths):
        self.page.wait_for_selector(selector, state="visible")
        self.page.set_input_files(selector, file_paths)
        log.info("Set input files for %s -> %s", selector, file_paths)

    def clear(self, selector: str):
        self.fill(selector, "")
        log.info("Clear element: %s", selector)

    def click_by_index(self, selector: str, index: int):
        self.page.wait_for_selector(selector)
        elements = self.page.query_selector_all(selector)

        if index >= len(elements):
            raise IndexError(
                f"Element '{selector}' at index {index} not found "
                f"(found {len(elements)})"
            )
        log.info("Click element: %s at index %s", selector, index)
        elements[index].click()


    # ===== Reads =====
    def text(self, selector: str) -> str:
        self.page.wait_for_selector(selector)
        text = self.page.inner_text(selector)
        log.info("Read text from %s: %s", selector, text)
        return text

    def input_value(self, selector: str) -> str:
        self.page.wait_for_selector(selector)
        value = self.page.input_value(selector)
        log.info("Input value from %s: %s", selector, value)
        return value

    def is_visible(self, selector: str) -> bool:
        try:
            visible = self.page.is_visible(selector)
            log.info("Is visible %s -> %s", selector, visible)
            return visible
        except Exception as e:
            log.info("Visibility check failed for %s: %s", selector, e)
            return False


    # ===== Waits =====
    def wait_visible(self, selector: str):
        log.info("Wait visible: %s", selector)
        self.page.wait_for_selector(selector, state="visible")

    def wait_hidden(self, selector: str):
        log.info("Wait hidden: %s", selector)
        self.page.wait_for_selector(selector, state="hidden")

    def wait_network_idle(self):
        log.info("Wait for network idle")
        self.page.wait_for_load_state("networkidle")


    # ===== JS =====
    def evaluate(self, script: str):
        log.info("Evaluate JS: %s", script)
        return self.page.evaluate(script)

    def query_all_texts(self, selector: str) -> list[str]:
        self.page.wait_for_selector(selector)
        elements = self.page.query_selector_all(selector)
        texts = [el.inner_text() for el in elements]
        return texts


    # ===== Additional generic helpers ====
    def get_attribute(self, selector: str, attribute: str) -> str:
        """Get the value of a specified attribute for an element."""
        self.page.wait_for_selector(selector)
        attr = self.page.get_attribute(selector, attribute)
        log.info("Get attribute '%s' from %s: %s", attribute, selector, attr)
        return attr
    
    
    # ===== Helpers for special controls =====
    def click_hidden_input(self, selector: str):
        self.page.wait_for_selector(selector)
        self.page.eval_on_selector(selector, "el => el.click()")
        log.info("Click hidden input via JS: %s", selector)

    def select_react_option(self, container_selector: str, value: str):
        self.click(container_selector)
        input_locator = self.page.locator(f"{container_selector} input[id^='react-select']")
        input_locator.wait_for(state="visible")
        input_locator.fill(value)
        input_locator.press("Enter")
        log.info("Select react option '%s' in %s", value, container_selector)