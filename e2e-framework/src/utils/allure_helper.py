import allure
import logging

log = logging.getLogger(__name__)

class AllureHelper:
    @staticmethod
    def attach_screenshot(page, name: str = "Screenshot"):
        try:
            png = page.screenshot(full_page=True)
            if isinstance(png, (bytes, bytearray)):
                allure.attach(png, name=name, attachment_type=allure.attachment_type.PNG)
            else:
                allure.attach.file(str(png), name=name, attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            log.warning(f"Failed to attach screenshot: {e}")

    @staticmethod
    def attach_api_response(response, name: str = "API Response"):
        try:
            status = getattr(response, "status_code", None)
            headers = getattr(response, "headers", None)
            body = getattr(response, "text", None)

            if status is not None:
                allure.attach(str(status), name=f"{name} - Status", attachment_type=allure.attachment_type.TEXT)

            if headers is not None:
                try:
                    import json
                    h_text = json.dumps(dict(headers), indent=2, ensure_ascii=False)
                except Exception:
                    h_text = str(headers)
                allure.attach(h_text, name=f"{name} - Headers", attachment_type=allure.attachment_type.JSON)

            if body is not None:
                allure.attach(body, name=f"{name} - Body", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            log.warning(f"Failed to attach API response: {e}")