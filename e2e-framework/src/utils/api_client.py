import logging
import requests
from src.utils.allure_helper import AllureHelper

log = logging.getLogger(__name__)

class APIClient:
    def __init__(self, base_url: str, default_headers: dict | None = None):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update(default_headers or {})


    # === Core Request ===
    def _request(self, method: str, endpoint: str, **kwargs):
        url = f"{self.base_url}{endpoint}"

        log.info("API %s %s", method.upper(), url)
        if "json" in kwargs:
            log.debug("Request JSON: %s", kwargs["json"])
        if "params" in kwargs:
            log.debug("Request params: %s", kwargs["params"])

        response = self.session.request(method, url, **kwargs)

        log.info("API response %s %s", response.status_code, url)
        log.debug("Response body: %s", response.text)

        AllureHelper.attach_api_response(
            response,
            name=f"{method.upper()} {endpoint}"
        )

        return response


    # === HTTP Methods ===
    def get(self, endpoint: str, **kwargs):
        return self._request("get", endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs):
        return self._request("post", endpoint, **kwargs)

    def put(self, endpoint: str, **kwargs):
        return self._request("put", endpoint, **kwargs)

    def delete(self, endpoint: str, **kwargs):
        return self._request("delete", endpoint, **kwargs)