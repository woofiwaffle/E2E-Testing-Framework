import os
import logging
from playwright.sync_api import sync_playwright, Browser, Page, Playwright, BrowserContext
from typing import Tuple, Optional
from src.utils.config_reader import get_config

log = logging.getLogger(__name__)

def open_page(test_name: Optional[str] = None) -> Tuple[Playwright, Browser, BrowserContext, Page, dict]:
    
    # ===== LOADING CONFIGURATION =====
    cfg = get_config()
    log.info("Starting Playwright")
    pw = sync_playwright().start()
    

    # ===== BROWSER SETTINGS =====
    browser_name = cfg["browser"]
    headless = cfg["headless"]
    slow_mo = cfg["slow_mo"]
    
    launch_args = {"headless": headless}
    if slow_mo > 0:
        launch_args["slow_mo"] = slow_mo
    if "launch_args" in cfg:
        launch_args.update(cfg["launch_args"])
    

    # ===== LAUNCHING THE BROWSER =====
    log.debug("Launching browser: %s (headless=%s)", browser_name, headless)
    browser = getattr(pw, browser_name).launch(**launch_args)
    

    # ===== CONTEXT SETTING =====
    viewport = cfg["viewport"]
    context_args = {"viewport": viewport}
    log.debug("Creating browser context with viewport=%s", viewport)
    context = browser.new_context(**context_args)
    

    # ===== CREATING A PAGE =====
    log.debug("Opening new page")
    page = context.new_page()


    # ===== SETTING TIMEOUT =====
    timeout = cfg["timeouts"]["default"]
    page.set_default_timeout(timeout)
    log.debug("Browser page ready")
    

    # ===== CREATION OF ARTIFACTS =====
    artifacts = {
        "test_dir": os.path.join(os.environ.get("REPORTS_DIR", "reports"), test_name or "default")
    }
    os.makedirs(artifacts["test_dir"], exist_ok=True)
    
    return pw, browser, context, page, artifacts