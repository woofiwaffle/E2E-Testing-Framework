import pytest
import os
from src.core.browser_factory import open_page
from src.utils.config_reader import get_config
from src.pages.example_page import ExamplePage
from src.utils.allure_helper import attach_screenshot, attach_page_source
import allure

@pytest.fixture(scope="session")
def config():
    return get_config()

@pytest.fixture(scope="function")
def browser_ctx(request, config):
    """
    Запускает браузер + context + page.
    Если в конфиге trace=True — стартуем tracing через context.tracing.start(...)
    По завершении — вызываем context.tracing.stop(path=...) чтобы сохранить trace.zip.
    """
    test_name = request.node.name
    pw, browser, context, page, artifacts = open_page(test_name=test_name)

    # start tracing if requested (correct API)
    if config.get("trace", False):
        # start tracing BEFORE performing actions
        # screenshots/snapshots/sources — рекомендованные опции для отладки
        context.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield page, artifacts

    # teardown: stop tracing if started
    if config.get("trace", False):
        trace_path = f"{artifacts['test_dir']}/trace.zip"
        try:
            context.tracing.stop(path=trace_path)
            # опционально — прикрепить trace.zip к Allure (в бинарном виде)
            try:
                with open(trace_path, "rb") as f:
                    allure.attach(f.read(), name=f"{request.node.name}_trace.zip", attachment_type=allure.attachment_type.ZIP)
            except Exception:
                # если attach ZIP не поддерживается в этой версии, можно пропустить
                pass
        except Exception as e:
            print("Failed to stop tracing:", e)

    # close context / browser / playwright
    try:
        context.close()
    except Exception:
        pass
    try:
        browser.close()
    except Exception:
        pass
    try:
        pw.stop()
    except Exception:
        pass

@pytest.fixture(scope="function")
def example_page(browser_ctx, config):
    page, meta = browser_ctx
    return ExamplePage(page, config.get("base_url"))

# hook: при падении теста — делать скриншот и прикреплять в allure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        page_fixt = item.funcargs.get("browser_ctx")
        if page_fixt:
            page, artifacts = page_fixt
            try:
                attach_screenshot(page, name=f"{item.name}_failure")
                attach_page_source(page, name=f"{item.name}_source")
            except Exception as e:
                print("Failed to attach artifacts:", e)
