import pytest
from src.utils.allure_helper import *

@pytest.mark.app_demoapp
@pytest.mark.ui
@pytest.mark.regression
@pytest.mark.priority_critical
@pytest.mark.severity_blocker
@allure.description("WHEN user opens the home page THEN all necessary DOM elements should be present")
def test_all_dom_elements_present(demoapp_page):
    # prepare
    demoapp_page.open_home()

    # verification
    assert demoapp_page.page.is_visible("h1"), "Header is not visible"
    assert demoapp_page.page.is_visible("input#demo-input"), "Demo input is not visible"
    assert demoapp_page.page.is_visible("button#demo-button"), "Demo button is not visible"
    assert demoapp_page.page.is_visible("#result"), "Result element is not visible"
    assert demoapp_page.page.is_visible("button#open-modal"), "Open modal button is not visible"
    assert demoapp_page.page.is_visible("button#show-toast"), "Show toast button is not visible"
    assert demoapp_page.page.is_visible("#simple-form"), "Simple form is not visible"
    assert demoapp_page.page.is_visible("#simple-input"), "Simple input is not visible"
    assert demoapp_page.page.is_visible("button[type='submit']"), "Submit button is not visible"
    assert demoapp_page.page.is_visible("#simple-list"), "Simple list is not visible"
    assert demoapp_page.page.is_visible("#new-item-input"), "New item input is not visible"
    assert demoapp_page.page.is_visible("#add-item-btn"), "Add item button is not visible"
    assert demoapp_page.page.is_visible("#theme-toggle"), "Theme toggle button is not visible"