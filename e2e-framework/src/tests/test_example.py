from src.core.page_factory import PageFactory

def test_home_page_with_components(browser_ctx, config):
    page, _ = browser_ctx
    example_page = PageFactory.get_page("example", page, config.get("base_url"))

    example_page.open_home()
    assert example_page.header_text() == "Demo Home Page"

    example_page.fill_demo_input("Hello Components")
    example_page.click_demo_button()