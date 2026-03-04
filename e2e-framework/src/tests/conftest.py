import pytest
import time
import requests
import logging
from src.core.browser_factory import open_page
from src.utils.allure_helper import *
from src.utils.config_reader import get_config
from src.utils.api_client import APIClient
from src.pages.demoapp_page import DemoAppPage
from src.pages.demoqa_page import DemoQAFormPage

log = logging.getLogger(__name__)


@pytest.fixture(scope="session")
def config(request):
    config_name = request.config.getoption("--config")
    return get_config(config_name)

def pytest_addoption(parser):
    parser.addoption(
        "--config",
        action="store",
        default=None,
        help="Config file name from config/ directory"
    )

# ===== ENVIRONMENTAL FIXTURES =====
@pytest.fixture(scope="function")
def wait_for_service(config):
    base = config["base_url"].rstrip("/")
    health_url = f"{base}/healthz"
    timeout = config["timeouts"]["service_wait"]
    interval = 0.5
    end = time.time() + timeout
    last_exc = None
    
    while time.time() < end:
        try:
            request_timeout = config["timeouts"]["healthcheck"]
            r = requests.get(health_url, timeout=request_timeout)
            if r.status_code == 200:
                return True
        except Exception as e:
            last_exc = e
        time.sleep(interval)
    
    raise RuntimeError(f"Service {health_url} did not become ready within {timeout}s. Last error: {last_exc}")


# ===== BROWSER FIXTURES =====
@pytest.fixture(scope="function")
def browser_ctx(request):
    test_name = request.node.name
    pw, browser, context, page, artifacts = open_page(test_name=test_name)
    try:
        page.on("console", lambda msg: log.info(f"[PAGE][console][{msg.type}] {msg.text}"))
    except Exception:
        pass

    try:
        def on_request_failed(req):
            log.warning(f"[PAGE][requestfailed] {req.url} - {req.failure}")
        page.on("requestfailed", on_request_failed)
    except Exception:
        pass

    yield page, artifacts

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


# ===== PAGE FIXTURES =====
@pytest.fixture(scope="function")
def demoapp_page(browser_ctx, config):
    page, meta = browser_ctx
    return DemoAppPage(page, config["base_url"])

@pytest.fixture(scope="function")
def demoqa_form_page(browser_ctx, config):
    page, meta = browser_ctx
    return DemoQAFormPage(page, config["base_url"])


# ===== API CLIENT =====
@pytest.fixture(scope="function")
def api_client(config):
    return APIClient(
        base_url=config["base_url"],
        default_headers={
            "Content-Type": "application/json"
        }
    )


# ===== ALLURE INTEGRATION =====
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call":
        return

    page = None
    artifacts = None

    for fixture_name in ("browser_ctx",):
        if fixture_name in item.fixturenames:
            page, artifacts = item.funcargs.get(fixture_name, (None, None))
    
    if report.failed:
        log.error(f"Test failed: {item.name}")
        if page:
            try:
                AllureHelper.attach_screenshot(page, "Failure screenshot")
            except Exception as e:
                log.warning("Failed to attach failure screenshot: %s", e)
        
        allure.attach(
            str(report.longrepr), 
            name="Failure details", 
            attachment_type=allure.attachment_type.TEXT
        )
    elif page:
        AllureHelper.attach_screenshot(page, "End of test screenshot")


# ===== TEST LIFECYCLE HOOKS =====
def pytest_runtest_setup(item):

    # === Allure markers ===
    for marker in item.iter_markers():
        name = marker.name

        if name in ("smoke", "api", "ui", "regression"):
            allure.dynamic.tag(name)

        if name.startswith("priority_"):
            priority_val = name.replace("priority_", "").upper()
            allure.dynamic.label("priority", priority_val)

        if name.startswith("severity_"):
            sev = name.replace("severity_", "").upper()
            allure.dynamic.severity(sev.lower())
    
    # === Logging ===
    log.info("=" * 80)
    log.info("START TEST: %s", item.nodeid)


def pytest_runtest_teardown(item):
    log.info("END TEST: %s", item.nodeid)