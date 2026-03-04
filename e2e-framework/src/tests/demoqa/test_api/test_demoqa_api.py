import pytest
import allure

@pytest.mark.app_demoqa
@pytest.mark.api
@pytest.mark.smoke
@pytest.mark.priority_high
@pytest.mark.severity_critical
@allure.description("WHEN user requests DemoQA home page THEN page should be available")
def test_demoqa_home_available(api_client):
    # action
    response = api_client.get("/")

    # verification
    assert response.status_code == 200
    assert "<title>demosite</title>" in response.text


@pytest.mark.app_demoqa
@pytest.mark.api
@pytest.mark.regression
@pytest.mark.priority_medium
@pytest.mark.severity_normal
@allure.description("WHEN user requests practice form page THEN form page should load")
def test_demoqa_form_page_available(api_client):
    # action
    response = api_client.get("/automation-practice-form")

    # verification
    assert response.status_code == 200
    assert "<div id=\"root\">" in response.text