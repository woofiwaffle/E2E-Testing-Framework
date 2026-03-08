# E2E Testing Framework — Project Documentation

## Introduction

This project implements an automated testing framework for web applications.

The main goal of the project is to design a reusable framework that supports:

- automated UI testing
- automated API testing
- containerized execution
- CI/CD integration
- test reporting

The framework is implemented using Python and modern test automation tools.

---

# Technology Stack

- Python 3
- Pytest
- Playwright
- Docker / Docker Compose
- Allure Reports
- GitHub Actions (CI/CD)

Additional libraries:

- requests
- pyyaml
- faker

---

# Architecture

The system contains three main components:

1. **Demo Application**
2. **E2E Testing Framework**
3. **Documentation and CI/CD configuration**

Project structure:

```
demo-app/
e2e-framework/
docs/
docker-compose.yml
```

---

# Demo Application

The `demo-app` directory contains a lightweight web application used as the system under test.

It includes:

- HTML interface
- simple JavaScript logic
- minimal backend server

This allows stable and reproducible UI and API tests.

---

# E2E Framework

The framework itself is located in the `e2e-framework` directory.

Main components:

## Components

Reusable UI elements:

- buttons
- inputs

## Core

Core utilities such as browser initialization.

Example:

- BrowserFactory

## Locators

Contains selectors used for UI testing.

Separate locator files are created for different applications.

## Pages

Implements **Page Object Model** design pattern.

Each page class represents a specific web page.

## Tests

Test suites divided into:

- API tests
- UI tests

Each test group targets a specific application.

---

# Configuration System

Framework configuration is stored in YAML files.

Example configurations:

- demoapp.local.yaml
- demoapp.docker.yaml
- demoqa.local.yaml

Configuration allows switching environments easily.

---

# Test Execution

Tests are executed using Pytest.

Examples:

```
pytest
pytest -k api
pytest -m app_demoapp
```

---

# Docker Integration

The entire environment can be started using Docker.

```
docker compose build
docker compose up
```

This ensures the same environment for all developers and CI pipelines.

---

# Test Reports

Allure is used for generating interactive reports.

```
allure serve reports/allure-results
```

Reports include:

- test results
- execution timeline
- logs
- attachments

---

# Continuous Integration

GitHub Actions pipeline automatically:

1. builds containers
2. runs tests
3. stores artifacts

---

# Future Improvements

Possible future extensions:

- parallel test execution
- integration with test management systems
- automatic defect creation
- performance testing support