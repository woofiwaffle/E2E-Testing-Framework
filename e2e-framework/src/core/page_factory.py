# src/core/page_factory.py
from src.pages.example_page import ExamplePage

class PageFactory:
    """
    Централизованная фабрика страниц.
    Позволяет получать любую зарегистрированную страницу по имени.
    """
    _pages = {
        "example": ExamplePage,
        # сюда можно добавлять новые страницы
    }

    @staticmethod
    def get_page(name: str, page, base_url):
        cls = PageFactory._pages.get(name)
        if not cls:
            raise ValueError(f"Unknown page: {name}")
        return cls(page, base_url)