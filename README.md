## E2E Testing Framework

Framework for end‑to‑end (E2E) testing of web applications using containerization.

The project demonstrates how automated browser and API tests can be executed in a reproducible environment using Docker, Playwright, Pytest, and Allure reporting.

---

### Project Overview

The repository contains:

- **demo-app** — a simple web application used as a system under test (SUT)
- **e2e-framework** — automated testing framework for UI and API tests
- **docker-compose** — containerized environment for running the application and tests
- **GitHub Actions CI/CD** — automated execution of tests in the pipeline
- **Allure reports** — visual test execution reports

The framework is designed to be **universal**, meaning it can be adapted to test different web applications by configuring locators, page objects, and environment settings.

---

## Quick Start

### Build Docker containers

```bash
docker compose -f docker-compose.yml build
```

### Start the environment for DemoApp

```bash
docker compose up -d demo-app

docker compose up e2e-demoapp
```

This command starts:

- demo application
- the container running end-to-end tests for DemoApp

### Start the environment for DemoQA

```bash
docker compose up e2e-demoqa
```

This command starts:

- the container running end-to-end tests for the external web application DemoQA

---

## Running Tests Manually (Examples)

Activate virtual environment (Windows PowerShell):

```bash
. .\.venv\Scripts\Activate.ps1
```

Run only API tests for DemoApp:

```bash
pytest -k api -s -m app_demoapp --config=demoapp.local.yaml
```

Run only UI tests for DemoApp:
```bash
pytest -k ui -s -m app_demoapp --config=demoapp.local.yaml
```

Run DemoApp tests:

```bash
pytest -m app_demoapp --config=demoapp.local.yaml
```

Run DemoQA tests:

```bash
pytest -m app_demoqa --config=demoqa.local.yaml
```

---

## Allure Report

Before using Allure ensure:

- Java is installed
- Allure CLI is available in PATH

Generate and open report:

```bash
allure serve reports/allure-results
```

---

## Docker Commands

Stop environment:

```bash
docker compose down -v --remove-orphans
```

Rebuild images without cache:

```bash
docker compose build --no-cache
```

---

## Notes

The primary test suite is executed against a **local demo application**, which provides a stable and reproducible testing environment.

Additionally, the framework is demonstrated on an **external web application (DemoQA)** to show that the framework can be applied to third-party systems without modifying the core architecture.

This approach highlights the flexibility and portability of the testing framework.

---