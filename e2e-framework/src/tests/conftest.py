import pytest
import os
import time
import requests
from src.core.browser_factory import open_page
from src.utils.config_reader import get_config
from src.pages.example_page import ExamplePage
from src.utils.artifacts_helper import save_screenshot, save_page_source, list_videos

@pytest.fixture(scope="session")
def config():
    return get_config()

@pytest.fixture(scope="function")
def wait_for_service(config):
    base = config.get("base_url").rstrip("/")
    health_url = f"{base}/healthz"
    timeout = config.get("service_wait_seconds", 30)
    interval = 0.5
    end = time.time() + timeout
    last_exc = None
    while time.time() < end:
        try:
            r = requests.get(health_url, timeout=2)
            if r.status_code == 200:
                return True
        except Exception as e:
            last_exc = e
        time.sleep(interval)
    raise RuntimeError(f"Service {health_url} did not become ready within {timeout}s. Last error: {last_exc}")

@pytest.fixture(scope="function")
def browser_ctx(request, config, wait_for_service):
    test_name = request.node.name
    pw, browser, context, page, artifacts = open_page(test_name=test_name)

    # DEBUG: печатаем console.log() из страницы в логи контейнера
    try:
        page.on("console", lambda msg: print(f"[PAGE][console][{msg.type}] {msg.text}"))
    except Exception:
        pass

    # DEBUG: печатаем упавшие запросы
    try:
        def on_request_failed(req):
            print(f"[PAGE][requestfailed] {req.url} - {req.failure}")
        page.on("requestfailed", on_request_failed)
    except Exception:
        pass

    # start tracing if requested
    if config.get("trace", False):
        context.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield page, artifacts

    # teardown: stop tracing if started
    if config.get("trace", False):
        trace_path = os.path.join(artifacts["test_dir"], "trace.zip")
        try:
            context.tracing.stop(path=trace_path)
        except Exception as e:
            print("Failed to stop tracing:", e)

    # optionally list videos
    if config.get("record_video", False):
        video_dir = artifacts.get("video_dir")
        if video_dir:
            videos = list_videos(video_dir)
            if videos:
                print(f"Saved videos for {test_name}: {videos}")

    # close
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

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        page_fixt = item.funcargs.get("browser_ctx")
        if page_fixt:
            page, artifacts = page_fixt
            try:
                save_screenshot(page, artifacts["test_dir"], name=f"{item.name}_failure")
                save_page_source(page, artifacts["test_dir"], name=f"{item.name}_source")
            except Exception as e:
                print("Failed to save artifacts:", e)
