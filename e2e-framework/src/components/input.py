from src.pages.base_page import BasePage

class Input(BasePage):
    def fill(self, selector: str, value: str):
        super().fill(selector, value)
    
    def set_file(self, selector: str, file_path):
        super().set_input_files(selector, file_path)