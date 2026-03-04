## Project Structure

### Root

- `.github/workflows/` — GitHub Actions CI/CD pipelines
  - `e2e-tests.yml`

- `.dockerignore`
- `.gitignore` 
- `docker-compose.yml`
- `README.md` — General information about the project and launch

### Demo Application

- `demo-app/` — source of the demo application
  - `public/` — static assets
      - `index.html`
      - `script.js` 
      - `styles.css`
  - `.dockerignore`
  - `Dockerfile` 
  - `package.json` 
  - `server.js` — main server entry point 

### Documentation

- `docs/` — project documentation
  - `Annotation_Old.pdf`
  - `PROJECT_PLAN.md` 
  - `README.md` 

### End‑to‑End Testing Framework

- `e2e-framework/` — framework for automated browser tests
  - `config/` — configuration files
    - `demoapp.docker.yaml`
    - `demoapp.local.yaml` 
    - `demoqa.local.yaml`
  - `logs/` 
  - `reports/` — Allure report output directory
  - `src/` — source code of the framework
    - `__init__.py`
    - `components/` — UI components
      - `__init__.py`
      - `button.py`
      - `input.py`
    - `core/` — core utilities
      - `__init__.py`
      - `browser_factory.py` — browser factory helper
    - `locators/`
      - `__init__.py`
      - `demoapp_locators.py`
      - `demoqa_locators.py`
    - `pages/` — page‑object models
      - `__init__.py` 
      - `base_page.py`
      - `demoapp_page.py`
      - `demoqa_page.py` 
    - `tests/` — test suites
      - `__init__.py` 
      - `demoapp/` — DemoApp specific tests
        - `__init__.py`
        - `test_api/` — API tests for DemoApp
          - `__init__.py` — 
          - `test_api_404.py` 
          - `test_api_echo.py` 
          - `test_api_healthcheck.py` 
          - `test_api_items.py` 
          - `test_api_toast.py` 
        - `test_ui/` — UI tests for DemoApp
          - `__init__.py` — 
          - `test_demo_form.py` 
          - `test_dom_elements.py` 
          - `test_modal_toast.py` 
          - `test_simple_form.py`
          - `test_simple_list.py`
          - `test_toggle_theme.py`
      - `demoqa/` — DemoQA specific tests
        - `__init__.py` 
        - `test_api/` — API tests for DemoQA
          - `__init__.py` 
          - `test_demoqa_api.py`
        - `test_ui/` — UI tests for DemoQA
          - `__init__.py`  
          - `test_demoqa_form.py` 
      - `conftest.py`
      - `utils/` — helper utilities
        - `__init__.py` 
        - `allure_helper.py` — helper functions for Allure reporting
        - `api_client.py` — wrapper for API client calls
        - `config_reader.py` — reads configuration files
  - `.dockerignore`
  - `Dockerfile`
  - `entrypoint.sh` — setup script that waits for `demo-app` and runs pytest with Allure
  - `pytest.ini` — pytest configuration file
  - `requirements.txt`  