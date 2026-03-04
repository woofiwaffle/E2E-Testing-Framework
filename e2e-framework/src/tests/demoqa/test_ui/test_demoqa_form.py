import pytest
import allure

@pytest.mark.app_demoqa
@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.priority_high
@pytest.mark.severity_critical
@allure.description("WHEN user opens practice form THEN form should be visible")
def test_demoqa_form_open(demoqa_form_page):
    # action
    demoqa_form_page.open()

    # verification
    assert demoqa_form_page.is_visible(
        demoqa_form_page.locators.FORM_HEADER
    )

@pytest.mark.app_demoqa
@pytest.mark.ui
@pytest.mark.regression
@pytest.mark.priority_high
@pytest.mark.severity_critical
@allure.description("WHEN user submits form with valid data THEN success modal should appear")
def test_demoqa_form_submit_success(demoqa_form_page):
    # prepare
    data = {
        "firstName": "Ivan",
        "lastName": "Petrov",
        "email": "ivan.petrov@test.com",
        "gender": "Male",
        "mobileNumber": "9998887776",
        "dateOfBirth": "08 Feb 1996",
        "subjects": ["Maths", "Physics"],
        "hobbies": ["Sports", "Music"],
        "currentAddress": "Moscow, Red Square",
        "state": "Haryana",
        "city": "Karnal",
    }

    demoqa_form_page.open()

    # action
    demoqa_form_page.fill_form(data)
    demoqa_form_page.submit()

    # verification
    success = demoqa_form_page.get_success_message()
    assert "Thanks for submitting the form" in success

@pytest.mark.app_demoqa
@pytest.mark.ui
@pytest.mark.regression
@pytest.mark.priority_medium
@pytest.mark.severity_normal
@allure.description("WHEN user submits empty form THEN form should not be submitted")
def test_demoqa_form_empty_submit(demoqa_form_page):
    # prepare
    demoqa_form_page.open()

    # action
    demoqa_form_page.submit()

    # verification
    assert not demoqa_form_page.is_visible(
        demoqa_form_page.locators.SUCCESS_MESSAGE
    )

@pytest.mark.app_demoqa
@pytest.mark.ui
@pytest.mark.regression
@pytest.mark.priority_medium
@pytest.mark.severity_minor
@allure.description("WHEN user enters invalid email THEN form should not be submitted")
def test_demoqa_form_invalid_email(demoqa_form_page):
    # prepare
    data = {
        "firstName": "Ivan",
        "lastName": "Petrov",
        "email": "invalid-email",
        "gender": "Male",
        "mobileNumber": "9998887776",
        "currentAddress": "Test address",
    }

    demoqa_form_page.open()

    # action
    demoqa_form_page.fill_form(data)
    demoqa_form_page.submit()

    # verification
    assert not demoqa_form_page.is_visible(
        demoqa_form_page.locators.SUCCESS_MESSAGE
    )

@pytest.mark.app_demoqa
@pytest.mark.ui
@pytest.mark.regression
@pytest.mark.priority_medium
@pytest.mark.severity_normal
@allure.description("WHEN user selects state THEN city list should update")
def test_demoqa_state_city_dependency(demoqa_form_page):
    # prepare
    demoqa_form_page.open()

    # action
    demoqa_form_page.select_state("Haryana")
    demoqa_form_page.select_city("Karnal")

    # verification
    assert True  