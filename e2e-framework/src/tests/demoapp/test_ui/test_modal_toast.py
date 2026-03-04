import pytest
from src.utils.allure_helper import *

@pytest.mark.app_demoapp
@pytest.mark.ui
@pytest.mark.regression
@pytest.mark.priority_normal
@pytest.mark.severity_medium
@allure.description("WHEN user opens the modal THEN the modal should be visible")
def test_modal_open(demoapp_page):
    # prepare
    demoapp_page.open_home()

    # action
    demoapp_page.click_open_modal()

    # verification
    assert demoapp_page.is_modal_visible(), "Modal did not open"

@pytest.mark.app_demoapp
@pytest.mark.ui
@pytest.mark.regression
@pytest.mark.priority_normal
@pytest.mark.severity_medium
@allure.description("WHEN user closes the modal THEN the modal should not be visible")
def test_modal_close(demoapp_page):
    # prepare
    demoapp_page.open_home()
    demoapp_page.click_open_modal()

    # action
    demoapp_page.click_close_modal()

    # verification
    assert not demoapp_page.is_modal_visible(), "Modal did not close"

@pytest.mark.app_demoapp
@pytest.mark.ui
@pytest.mark.regression
@pytest.mark.priority_normal
@pytest.mark.severity_medium
@allure.description("WHEN user shows the toast notification THEN the toast should be visible")
def test_toast_appear(demoapp_page):
    # prepare
    demoapp_page.open_home()

    # action
    demoapp_page.click_show_toast()

    # verification
    assert demoapp_page.is_toast_visible(), "Toast did not appear"

@pytest.mark.app_demoapp
@pytest.mark.ui
@pytest.mark.regression
@pytest.mark.priority_normal
@pytest.mark.severity_medium
@allure.description("WHEN user waits for the toast to disappear THEN the toast should not be visible")
def test_toast_disappear(demoapp_page):
    # prepare
    demoapp_page.open_home()
    demoapp_page.click_show_toast()

    # action
    demoapp_page.wait_for_toast_disappear()

    # verification
    assert not demoapp_page.is_toast_visible(), "Toast did not disappear"