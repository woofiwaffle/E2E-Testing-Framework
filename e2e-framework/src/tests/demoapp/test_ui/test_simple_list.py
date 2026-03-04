import pytest
from src.utils.allure_helper import *

@pytest.mark.app_demoapp
@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.priority_high
@pytest.mark.severity_critical
@allure.description("WHEN user adds a new item to the list THEN the item should be added successfully and the list should be updated")
def test_add_item_to_list(demoapp_page):
    # prepare
    demoapp_page.open_home()
    initial_items = demoapp_page.get_list_items()
    initial_count = len(initial_items)

    # action
    demoapp_page.fill_new_item_input("New Test Item")
    demoapp_page.click_add_item_button()

    # verification
    result = demoapp_page.get_result_text()
    assert "New Test Item" in result, f"Expected 'New Test Item' in result, but got '{result}'"

    updated_items = demoapp_page.get_list_items()
    updated_count = len(updated_items)
    assert updated_count == initial_count + 1, f"Expected {initial_count + 1} items, but got {updated_count}"

@pytest.mark.app_demoapp
@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.priority_high
@pytest.mark.severity_critical
@allure.description("WHEN user deletes an item from the list THEN the item should be deleted successfully and the list should be updated")
def test_delete_item_from_list(demoapp_page):
    # prepare
    demoapp_page.open_home()
    initial_items = demoapp_page.get_list_items()
    initial_count = len(initial_items)

    if initial_count == 0:
        demoapp_page.fill_new_item_input("Item to Delete")
        demoapp_page.click_add_item_button()
        demoapp_page.get_result_text()
        initial_count = 1

    # action
    demoapp_page.click_delete_button(0)

    # verification
    result = demoapp_page.get_result_text()
    assert "deleted successfully" in result, f"Expected 'deleted successfully' in result, but got '{result}'"

    updated_items = demoapp_page.get_list_items()
    updated_count = len(updated_items)
    assert updated_count == initial_count - 1, f"Expected {initial_count - 1} items, but got {updated_count}"

@pytest.mark.app_demoapp
@pytest.mark.ui
@pytest.mark.regression
@pytest.mark.priority_high
@pytest.mark.severity_critical
@allure.description("WHEN user edits an item in the list THEN the item should be updated successfully and the list should be updated")
def test_edit_item_in_list(demoapp_page):
    # prepare
    demoapp_page.open_home()
    initial_items = demoapp_page.get_list_items()
    initial_count = len(initial_items)

    if initial_count == 0:
        demoapp_page.fill_new_item_input("Item to Edit")
        demoapp_page.click_add_item_button()
        demoapp_page.get_result_text()

    # action
    demoapp_page.click_edit_button(0)
    demoapp_page.wait_for_custom_prompt()
    demoapp_page.fill_custom_prompt_input("Edited Item")
    demoapp_page.click_custom_prompt_ok()

    # verification
    result = demoapp_page.get_result_text()
    assert "Item updated successfully" in result, f"Expected 'Item updated successfully' in result, but got '{result}'"

    updated_items = demoapp_page.get_list_items()
    assert "Edited Item" in updated_items[0], "Item was not updated correctly"

@pytest.mark.app_demoapp
@pytest.mark.ui
@pytest.mark.regression
@pytest.mark.priority_medium
@pytest.mark.severity_minor
@allure.description("WHEN user opens edit modal AND clicks Cancel THEN item name is not changed")
def test_cancel_edit(demoapp_page):
    # prepare
    demoapp_page.open_home()
    demoapp_page.fill_new_item_input("Test Item")
    demoapp_page.click_add_item_button()
    items_before = demoapp_page.get_list_items()
    
    # action
    demoapp_page.click_edit_button(0)
    demoapp_page.wait_for_custom_prompt()
    demoapp_page.click_custom_prompt_cancel()
    
    # verification
    items_after = demoapp_page.get_list_items()
    assert items_before == items_after, "Item name should not change after canceling edit"

@pytest.mark.app_demoapp
@pytest.mark.ui
@pytest.mark.regression
@pytest.mark.priority_medium
@pytest.mark.severity_normal
@allure.description("WHEN user adds item to list AND reloads the page THEN list should be loaded from server")
def test_local_storage_list_cache(demoapp_page):
    # prepare
    demoapp_page.open_home()
    demoapp_page.fill_new_item_input("Test Item")
    demoapp_page.click_add_item_button()
    
    # action
    demoapp_page.reload_page()
    
    # verification
    items = demoapp_page.get_list_items()
    assert any("Test Item" in item for item in items), "List should be loaded from server after reload"