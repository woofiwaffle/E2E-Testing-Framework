# src/tests/test_minimal.py
import pytest
from src.core.browser_factory import open_page

def test_basic_navigation():
    """Базовый тест навигации по example.com"""
    pw, browser, page = open_page()
    try:
        # Используем стандартный тестовый сайт
        page.goto("https://example.com")
        
        # Проверяем заголовок
        title = page.title()
        assert "Example" in title
        
        # Проверяем наличие основного контента
        heading = page.query_selector("h1")
        assert heading is not None
        assert "Example" in heading.inner_text()
        
    finally:
        browser.close()
        pw.stop()

def test_form_interaction():
    """Тест взаимодействия с формами на тестовом сайте"""
    pw, browser, page = open_page()
    try:
        # Используем сайт для тестирования форм
        page.goto("https://www.saucedemo.com/")
        
        # Заполняем форму логина
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")
        
        # Проверяем успешный логин
        page.wait_for_selector(".inventory_list")
        assert "inventory" in page.url
        
    finally:
        browser.close()
        pw.stop()