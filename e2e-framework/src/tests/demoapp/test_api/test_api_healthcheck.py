import pytest
import allure

@pytest.mark.app_demoapp
@pytest.mark.api
@pytest.mark.smoke
@pytest.mark.priority_critical
@pytest.mark.severity_blocker
@allure.description("WHEN user sends GET request to /healthz THEN response should contain success status")
def test_api_healthcheck_endpoint(api_client):
    # action
    response = api_client.get("/healthz")

    # verification
    assert response.status_code == 200
    assert response.text == "OK"