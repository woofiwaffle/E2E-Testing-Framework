import allure
import os
from datetime import datetime

def attach_screenshot(page, name: str = "screenshot"):
    """
    Делает скриншот страницы и прикрепляет к Allure.
    page — playwright Page.
    """
    ts = datetime.utcnow().strftime("%Y%m%dT%H%M%S")
    filename = f"{name}_{ts}.png"
    tmp_path = f"/tmp/{filename}"
    page.screenshot(path=tmp_path, full_page=True)
    with open(tmp_path, "rb") as f:
        allure.attach(f.read(), name=filename, attachment_type=allure.attachment_type.PNG)
    try:
        os.remove(tmp_path)
    except Exception:
        pass

def attach_page_source(page, name: str = "page_source"):
    ts = datetime.utcnow().strftime("%Y%m%dT%H%M%S")
    filename = f"{name}_{ts}.html"
    tmp_path = f"/tmp/{filename}"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(page.content())
    with open(tmp_path, "rb") as f:
        allure.attach(f.read(), name=filename, attachment_type=allure.attachment_type.HTML)
    try:
        os.remove(tmp_path)
    except Exception:
        pass
