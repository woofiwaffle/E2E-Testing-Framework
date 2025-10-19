from playwright.sync_api import sync_playwright, Browser, Page, Playwright, BrowserContext
from typing import Tuple, Optional
from src.utils.config_reader import get_config
from src.utils.logger import get_logger
import os
import uuid

log = get_logger("BrowserFactory")

def open_page(test_name: Optional[str] = None) -> Tuple[Playwright, Browser, BrowserContext, Page, dict]:
    """
    Возвращает (playwright, browser, context, page, meta).
    Не пытается ставить атрибуты на context — трассировку и запись видео
    нужно включать через методы context.tracing.start и context.tracing.stop в фикстурах.
    """
    cfg = get_config()
    pw = sync_playwright().start()
    browser_name = cfg.get("browser", "chromium")
    headless = cfg.get("headless", True)
    record_video = cfg.get("record_video", False)
    trace_on = cfg.get("trace", False)

    launch_args = {"headless": headless}
    log.info(f"Launching {browser_name} headless={headless} video={record_video} trace={trace_on}")

    browser = getattr(pw, browser_name).launch(**launch_args)

    # Context options (video dir if enabled)
    context_args = {}
    artifacts = {}
    run_id = test_name or str(uuid.uuid4())
    reports_dir = os.environ.get("REPORTS_DIR", "reports")
    test_dir = f"{reports_dir}/{run_id}"
    os.makedirs(test_dir, exist_ok=True)
    artifacts["test_dir"] = test_dir

    if record_video:
        video_dir = os.path.join(test_dir, "video")
        os.makedirs(video_dir, exist_ok=True)
        context_args["record_video_dir"] = video_dir
        artifacts["video_dir"] = video_dir

    context = browser.new_context(**context_args)
    page = context.new_page()
    page.set_default_timeout(cfg.get("timeouts", {}).get("default", 5000))

    return pw, browser, context, page, artifacts