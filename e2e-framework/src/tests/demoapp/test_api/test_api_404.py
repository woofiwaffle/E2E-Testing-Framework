import pytest
import allure

@pytest.mark.app_demoapp
@pytest.mark.api
@pytest.mark.regression
@pytest.mark.priority_medium
@pytest.mark.severity_minor
@allure.description("WHEN user sends GET request to non-existent endpoint THEN response should return 404 status code")
def test_api_404_endpoint(api_client):
    # prepare
    endpoint = "/api/non-existent"

    # action
    response = api_client.get(endpoint)

    # verification
    assert response.status_code == 404
    assert response.json()["message"] == "API endpoint not found"