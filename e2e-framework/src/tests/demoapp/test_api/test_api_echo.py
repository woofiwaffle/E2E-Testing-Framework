import pytest
import allure

@pytest.mark.app_demoapp
@pytest.mark.api
@pytest.mark.smoke
@pytest.mark.priority_high
@pytest.mark.severity_critical
@allure.description("WHEN user sends POST request to /api/echo THEN response should contain the sent data")
def test_api_echo_endpoint(api_client):
    # prepare
    payload = {"text": "Test API"}

    # action
    response = api_client.post("/api/echo", json=payload)

    # verification
    assert response.status_code == 200
    assert response.json()["data"] == payload["text"]

@pytest.mark.app_demoapp
@pytest.mark.api
@pytest.mark.regression
@pytest.mark.priority_medium
@pytest.mark.severity_normal
@allure.description("WHEN user sends POST request to /api/echo with empty data THEN response should contain empty data")
def test_api_echo_empty_data(api_client):
    # prepare
    payload = {"text": ""}
    
    # action
    response = api_client.post("/api/echo", json=payload)
    
    # verification
    assert response.status_code == 200
    assert response.json()["data"] == ""