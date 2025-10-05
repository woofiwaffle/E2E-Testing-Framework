from src.pages.base_page import BasePage
from typing import List

class Table(BasePage):
    """
    Компонент таблицы.
    """
    def get_rows_text(self, selector: str) -> List[str]:
        self.page.wait_for_selector(selector)
        elements = self.page.query_selector_all(selector)
        return [el.inner_text() for el in elements]