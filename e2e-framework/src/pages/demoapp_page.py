import allure
from src.pages.base_page import BasePage
from src.components.button import Button
from src.components.input import Input
from src.locators.demoapp_locators import DemoAppLocators

class DemoAppPage(BasePage):
    def __init__(self, page, base_url):
        super().__init__(page, base_url)
        self.input = Input(page, base_url)
        self.button = Button(page, base_url)
        self.locators = DemoAppLocators()

    @allure.step("Open home page")
    def open_home(self):
        self.open("/")
        self.wait_network_idle()
        self.wait_visible(self.locators.HEADER)

    @allure.step("Fill demo input: {value}")
    def fill_demo_input(self, value: str):
        self.input.fill(self.locators.INPUT_DEMO, value)

    @allure.step("Click demo button")
    def click_demo_button(self):
        self.button.click(self.locators.BUTTON_DEMO)

    @allure.step("Get result text")
    def get_result_text(self) -> str:
        return self.text(self.locators.RESULT)

    @allure.step("Fill simple form input: {value}")
    def fill_simple_form_input(self, value: str):
        self.input.fill(self.locators.SIMPLE_INPUT, value)

    @allure.step("Submit simple form")
    def submit_simple_form(self):
        self.button.click(self.locators.BUTTON_SIMPLE)

    @allure.step("Click open modal button")
    def click_open_modal(self):
        self.button.click(self.locators.OPEN_MODAL_BUTTON)

    @allure.step("Click close modal button")
    def click_close_modal(self):
        self.button.click(self.locators.CLOSE_MODAL_BUTTON)

    @allure.step("Check if modal is visible")
    def is_modal_visible(self) -> bool:
        return self.is_visible(self.locators.MODAL)

    @allure.step("Click show toast button")
    def click_show_toast(self):
        self.button.click(self.locators.SHOW_TOAST_BUTTON)

    @allure.step("Check if toast is visible")
    def is_toast_visible(self) -> bool:
        return self.is_visible(self.locators.TOAST)

    @allure.step("Wait for toast to disappear")
    def wait_for_toast_disappear(self):
        self.wait_hidden(self.locators.TOAST)

    @allure.step("Fill new item input: {value}")
    def fill_new_item_input(self, value: str):
        self.input.fill(self.locators.NEW_ITEM_INPUT, value)

    @allure.step("Click add item button")
    def click_add_item_button(self):
        self.button.click(self.locators.ADD_ITEM_BUTTON)

    @allure.step("Get list items")
    def get_list_items(self) -> list:
        return self.query_all_texts(f"{self.locators.SIMPLE_LIST} li")

    @allure.step("Click edit button at index {index}")
    def click_edit_button(self, index: int):
        self.click_by_index(self.locators.EDIT_BUTTON, index)

    @allure.step("Wait for custom prompt")
    def wait_for_custom_prompt(self):
        self.wait_visible(self.locators.CUSTOM_PROMPT_MODAL)

    @allure.step("Fill custom prompt input: {text}")
    def fill_custom_prompt_input(self, text: str):
        self.input.fill(self.locators.CUSTOM_PROMPT_INPUT, text)

    @allure.step("Click custom prompt OK button")
    def click_custom_prompt_ok(self):
        self.button.click(self.locators.CUSTOM_PROMPT_OK_BUTTON)

    @allure.step("Click custom prompt cancel button")
    def click_custom_prompt_cancel(self):
        self.button.click(self.locators.CUSTOM_PROMPT_CANCEL_BUTTON)

    @allure.step("Click delete button at index {index}")
    def click_delete_button(self, index: int):
        self.click_by_index(self.locators.DELETE_BUTTON, index)

    @allure.step("Toggle theme")
    def toggle_theme(self):
        self.button.click(self.locators.THEME_TOGGLE)

    @allure.step("Check if dark theme is enabled")
    def is_dark_theme(self) -> bool:
        return self.evaluate("document.body.classList.contains('dark-theme')")

    @allure.step("Reload page")
    def reload_page(self):
        self.reload()
        self.wait_network_idle()

    @allure.step("Get local storage item: {key}")
    def get_local_storage_item(self, key: str) -> str:
        return self.evaluate(f"localStorage.getItem('{key}')")

    @allure.step("Clear demo input")
    def clear_demo_input(self):
        self.input.fill(self.locators.INPUT_DEMO, "")

    @allure.step("Wait for loader to disappear")
    def wait_for_loader_disappear(self):
        self.wait_hidden(self.locators.LOADER)

    @allure.step("Get simple form input value")
    def get_simple_form_input_value(self) -> str:
        return self.input_value(self.locators.SIMPLE_INPUT)