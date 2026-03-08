# E2E Testing Framework

Framework for end‑to‑end (E2E) testing of web applications using containerization.

The project demonstrates how automated browser and API tests can be executed in a reproducible environment using Docker, Playwright, Pytest, and Allure reporting.

---

## Project Overview

The repository contains:

- **demo-app** — a simple web application used as a system under test (SUT)
- **e2e-framework** — automated testing framework for UI and API tests
- **docker-compose** — containerized environment for running the application and tests
- **GitHub Actions CI/CD** — automated execution of tests in the pipeline
- **Allure reports** — visual test execution reports

The framework is designed to be **universal**, meaning it can be adapted to test different web applications by configuring locators, page objects, and environment settings.

---

# Quick Start

## Build Docker containers

```bash
docker compose -f docker-compose.yml build
```

## Start the environment

```bash
docker compose -f docker-compose.yml up
```

This command starts:

- demo application
- E2E test runner container

---

# Running Tests Manually

Activate virtual environment (Windows PowerShell):

```bash
. .\.venv\Scripts\Activate.ps1
```

Run all tests:

```bash
pytest
```

Run only API tests:

```bash
pytest -k api -s
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

# Allure Report

Before using Allure ensure:

- Java is installed
- Allure CLI is available in PATH

Generate and open report:

```bash
allure serve reports/allure-results
```

---

# Docker Commands

Stop environment:

```bash
docker compose down -v --remove-orphans
```

Rebuild images without cache:

```bash
docker compose build --no-cache
```

Start services:

```bash
docker compose up
```

Run specific services:

```bash
docker compose up -d demo-app
docker compose up e2e-demoapp
docker compose up e2e-demoqa
```

---

# Notes

Primary tests are executed against the **local demo-app** to ensure stability and reproducibility.

Additionally, tests can be executed against external applications to demonstrate framework flexibility.