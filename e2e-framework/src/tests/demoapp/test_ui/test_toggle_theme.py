import pytest
from src.utils.allure_helper import *

@pytest.mark.app_demoapp
@pytest.mark.ui
@pytest.mark.regression
@pytest.mark.priority_low
@pytest.mark.severity_minor
@allure.description("WHEN user toggles the theme THEN the theme should change from light to dark or vice versa")
def test_theme_toggle(demoapp_page):
    # Prepare
    demoapp_page.open_home()
    initial_is_dark = demoapp_page.is_dark_theme()

    # Action
    demoapp_page.toggle_theme()

    # Verification
    new_is_dark = demoapp_page.is_dark_theme()
    assert new_is_dark != initial_is_dark, f"Expected theme change, but theme remained {initial_is_dark}"

@pytest.mark.app_demoapp
@pytest.mark.ui
@pytest.mark.regression
@pytest.mark.priority_medium
@pytest.mark.severity_normal
@allure.description("WHEN user toggles theme THEN theme should be saved in localStorage")
def test_local_storage_theme_persistence(demoapp_page):
    # prepare
    demoapp_page.open_home()
    
    # action
    demoapp_page.toggle_theme()
    
    # verification
    theme_value = demoapp_page.get_local_storage_item("demo.theme")
    assert theme_value == "dark", "Theme should be saved in localStorage as 'dark'"

@pytest.mark.app_demoapp
@pytest.mark.ui
@pytest.mark.regression
@pytest.mark.priority_medium
@pytest.mark.severity_normal
@allure.description("WHEN user toggles theme AND reloads the page THEN theme should persist")
def test_theme_persistence_on_page_reload(demoapp_page):
    # prepare
    demoapp_page.open_home()
    
    # action
    demoapp_page.toggle_theme()
    is_dark_before_reload = demoapp_page.is_dark_theme()
    demoapp_page.reload_page()
    
    # verification
    is_dark_after_reload = demoapp_page.is_dark_theme()
    assert is_dark_before_reload == is_dark_after_reload, "Theme should persist after page reload"