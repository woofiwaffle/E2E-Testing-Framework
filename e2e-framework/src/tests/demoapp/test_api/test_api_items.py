import pytest
import allure

@pytest.mark.app_demoapp
@pytest.mark.api
@pytest.mark.regression
@pytest.mark.priority_medium
@pytest.mark.severity_normal
@allure.description("WHEN user sends GET request to /api/items THEN response should contain list of items")
def test_api_get_items(api_client):
    # action
    response = api_client.get("/api/items")

    # verification
    assert response.status_code == 200
    assert "data" in response.json()
    assert len(response.json()["data"]) > 0

@pytest.mark.app_demoapp
@pytest.mark.api
@pytest.mark.smoke
@pytest.mark.priority_high
@pytest.mark.severity_critical
@allure.description("WHEN user sends POST request to /api/items THEN new item should be added")
def test_api_add_item(api_client):
    # prepare
    payload = {"name": "New Item"}

    # action
    response = api_client.post("/api/items", json=payload)

    # verification
    assert response.status_code == 200
    assert response.json()["data"]["name"] == payload["name"]

@pytest.mark.app_demoapp
@pytest.mark.api
@pytest.mark.regression
@pytest.mark.priority_high
@pytest.mark.severity_critical
@allure.description("WHEN user sends PUT request to /api/items/:id THEN item should be updated")
def test_api_update_item(api_client):
    # prepare
    add_payload = {"name": "Test Item"}
    update_payload = {"name": "Updated Item"}

    add_response = api_client.post("/api/items", json=add_payload)
    assert add_response.status_code == 200
    item_id = add_response.json()["data"]["id"]

    # action
    response = api_client.put(
        f"/api/items/{item_id}",
        json=update_payload
    )

    # verification
    assert response.status_code == 200
    assert response.json()["data"]["name"] == update_payload["name"]

@pytest.mark.app_demoapp
@pytest.mark.api
@pytest.mark.regression
@pytest.mark.priority_high
@pytest.mark.severity_critical
@allure.description("WHEN user sends DELETE request to /api/items/:id THEN item should be deleted")
def test_api_delete_item(api_client):
    # prepare
    add_response = api_client.post(
        "/api/items",
        json={"name": "Test Item"}
    )
    assert add_response.status_code == 200
    item_id = add_response.json()["data"]["id"]

    # action
    response = api_client.delete(f"/api/items/{item_id}")

    # verification
    assert response.status_code == 200
    assert response.json()["message"] == "Item deleted"

@pytest.mark.app_demoapp
@pytest.mark.api
@pytest.mark.regression
@pytest.mark.priority_medium
@pytest.mark.severity_minor
@allure.description("WHEN user sends POST request to /api/items without name THEN response should return error")
def test_api_add_item_without_name(api_client):
    # prepare
    payload = {"name": ""}

    # action
    response = api_client.post("/api/items", json=payload)

    # verification
    assert response.status_code == 400
    assert response.json()["message"] == "Name required"