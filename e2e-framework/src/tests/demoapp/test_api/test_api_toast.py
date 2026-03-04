import pytest
import allure

@pytest.mark.app_demoapp
@pytest.mark.api
@pytest.mark.regression
@pytest.mark.priority_low
@pytest.mark.severity_minor
@allure.description("WHEN user sends GET request to /api/toast THEN response should contain toast message")
def test_api_toast_endpoint(api_client):
    # action
    response = api_client.get("/api/toast")

    # verification
    assert response.status_code == 200
    assert response.json()["message"] == "toast shown"