import pytest
from src.utils.allure_helper import *

@pytest.mark.app_demoapp
@pytest.mark.ui
@pytest.mark.regression
@pytest.mark.priority_medium
@pytest.mark.severity_normal
@allure.description("WHEN user submits demo form THEN response should be received within acceptable time")
def test_response_delay(demoapp_page):
    # prepare
    demoapp_page.open_home()
    demoapp_page.fill_demo_input("Test Input")
    
    # action
    start_time = demoapp_page.page.evaluate("Date.now()")
    demoapp_page.click_demo_button()
    demoapp_page.wait_for_loader_disappear()
    end_time = demoapp_page.page.evaluate("Date.now()")
    
    # verification
    response_time = end_time - start_time
    assert response_time < 5000, f"Response time should be less than 5 seconds, but was {response_time}ms"

@pytest.mark.app_demoapp
@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.priority_high
@pytest.mark.severity_critical
@allure.description("WHEN user submits the demo form with valid data THEN the form should be submitted successfully and the result should contain the submitted data")
def test_demoform_submission(demoapp_page):
    # prepare
    demoapp_page.open_home()

    # action
    demoapp_page.fill_demo_input("Test Demo Input")
    demoapp_page.click_demo_button()

    # verification
    result = demoapp_page.get_result_text()
    assert "Test Demo Input" in result, f"Expected 'Test Demo Input' in result, but got '{result}'"

@pytest.mark.app_demoapp
@pytest.mark.ui
@pytest.mark.regression
@pytest.mark.priority_medium
@pytest.mark.severity_normal
@allure.description("WHEN user submits the demo form with empty input THEN the form should show an error message")
def test_demoform_empty_input(demoapp_page):
    # prepare
    demoapp_page.open_home()

    # action
    demoapp_page.click_demo_button()

    # verification
    result = demoapp_page.get_result_text()
    assert "Please enter some text" in result, f"Expected 'Please enter some text' in result, but got '{result}'"

@pytest.mark.app_demoapp
@pytest.mark.ui
@pytest.mark.regression
@pytest.mark.priority_medium
@pytest.mark.severity_normal
@allure.description("WHEN user submits demo form twice THEN result updates with last value")
def test_demoform_resubmission_updates_result(demoapp_page):
    # prepare
    demoapp_page.open_home()
    demoapp_page.fill_demo_input("First Input")
    demoapp_page.click_demo_button()
    
    # action
    demoapp_page.fill_demo_input("Second Input")
    demoapp_page.click_demo_button()
    
    # verification
    result = demoapp_page.get_result_text()
    assert "Second Input" in result, "Result should update with last submitted value"

@pytest.mark.app_demoapp
@pytest.mark.ui
@pytest.mark.regression
@pytest.mark.priority_medium
@pytest.mark.severity_normal
@allure.description("WHEN user types new value after previous submit THEN previous result should not block new submit")
def test_demoform_clear_result_on_new_input(demoapp_page):
    # prepare
    demoapp_page.open_home()
    demoapp_page.fill_demo_input("First Input")
    demoapp_page.click_demo_button()
    
    # action
    demoapp_page.clear_demo_input()
    demoapp_page.fill_demo_input("New Input")
    demoapp_page.click_demo_button()
    
    # verification
    result = demoapp_page.get_result_text()
    assert "New Input" in result, "New input should be submitted successfully"