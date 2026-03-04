import pytest
from src.utils.allure_helper import *

@pytest.mark.app_demoapp
@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.priority_high
@pytest.mark.severity_critical
@allure.description("WHEN user submits the simple form with valid data THEN the form should be submitted successfully and the result should contain the submitted data")
def test_simple_form_submission(demoapp_page):
    # prepare
    demoapp_page.open_home()

    # action
    demoapp_page.fill_simple_form_input("Test Form Submission")
    demoapp_page.submit_simple_form()

    # verification
    result = demoapp_page.get_result_text()
    assert "Form submitted successfully: Test Form Submission" in result, f"Expected 'Form submitted successfully: Test Form Submission' in result, but got '{result}'"

@pytest.mark.app_demoapp
@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.priority_high
@pytest.mark.severity_critical
@allure.description("WHEN user submits simple form THEN input field should be cleared")
def test_simple_form_field_clearing(demoapp_page):
    # prepare
    demoapp_page.open_home()
    demoapp_page.fill_simple_form_input("Test Input")

    # action
    demoapp_page.submit_simple_form()

    # verification
    input_value = demoapp_page.get_simple_form_input_value()
    assert input_value == "", "Input field should be cleared after submission"
