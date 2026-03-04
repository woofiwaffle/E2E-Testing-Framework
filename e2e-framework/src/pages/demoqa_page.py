import allure
from playwright.sync_api import Page
from src.pages.base_page import BasePage
from src.components.button import Button
from src.components.input import Input
from src.locators.demoqa_locators import DemoQAFormLocators

class DemoQAFormPage(BasePage):
    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)
        self.input = Input(page, base_url)
        self.button = Button(page, base_url)
        self.locators = DemoQAFormLocators()

    @allure.step("Open the DemoQA registration form")
    def open(self) -> None:
        super().open("/automation-practice-form")
        self.wait_visible(self.locators.FORM_HEADER)

    @allure.step("Fill the form with the provided data")
    def fill_form(self, data: dict) -> None:
        self.input.fill(self.locators.FIRST_NAME, data["firstName"])
        self.input.fill(self.locators.LAST_NAME, data["lastName"])
        self.input.fill(self.locators.EMAIL, data["email"])

        if data.get("gender"):
            self.select_gender(data["gender"])

        self.input.fill(self.locators.MOBILE_NUMBER, data["mobileNumber"])

        if data.get("dateOfBirth"):
            self.input.fill(self.locators.DATE_OF_BIRTH, data["dateOfBirth"])


        for subject in data.get("subjects", []):
            self.input.fill(self.locators.SUBJECTS_INPUT, subject)
            self.press(self.locators.SUBJECTS_INPUT, "Enter")
        
        if data.get("hobbies"):
            self.select_hobbies(data["hobbies"])

        if data.get("filePath"):
            self.input.set_file(self.locators.UPLOAD_PICTURE, data["filePath"])

        self.input.fill(self.locators.CURRENT_ADDRESS, data["currentAddress"])

        if data.get("state"):
            self.select_state(data["state"])
        if data.get("city"):
            self.select_city(data["city"])

    @allure.step("Submit the form")
    def submit(self) -> None:
        self.button.click(self.locators.SUBMIT_BUTTON)

    @allure.step("Retrieve the success message text")
    def get_success_message(self) -> str:
        return self.text(self.locators.SUCCESS_MESSAGE).strip()
    

    # ===== additional helpers =====
    @allure.step("Select gender: {gender}")
    def select_gender(self, gender: str):
        mapping = {
            "Male": self.locators.GENDER_MALE,
            "Female": self.locators.GENDER_FEMALE,
            "Other": self.locators.GENDER_OTHER,
        }
        sel = mapping.get(gender)
        if not sel:
            raise ValueError(f"Unknown gender: {gender}")
        self.click_hidden_input(sel)

    @allure.step("Select hobbies: {hobbies}")
    def select_hobbies(self, hobbies: list):
        hobby_map = {
            "Sports": self.locators.HOBBIES_SPORTS,
            "Reading": self.locators.HOBBIES_READING,
            "Music": self.locators.HOBBIES_MUSIC,
        }
        for h in hobbies:
            sel = hobby_map.get(h)
            if not sel:
                raise ValueError(f"Unknown hobby: {h}")
            self.click_hidden_input(sel)

    @allure.step("Upload picture: {path}")
    def upload_picture(self, path: str):
        self.input.set_file(self.locators.UPLOAD_PICTURE, path)

    @allure.step("Select state: {state}")
    def select_state(self, state: str):
        self.select_react_option(self.locators.STATE, state)

    @allure.step("Select city: {city}")
    def select_city(self, city: str):
        self.select_react_option(self.locators.CITY, city)
