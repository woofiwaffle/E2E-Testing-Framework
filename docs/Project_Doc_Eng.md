## Framework for end—to-end testing - Project documentation

### Introduction

This project implements a framework for automated testing of web applications.

The main goal of the project is to develop a reusable environment that simplifies the creation, execution and analysis of end—to-end tests.

The testing environment is focused on providing a reproducible testing environment by combining automated browser testing with containerization technologies.

The system allows you to automate user interface and API testing, manage configuration, and integrate with modern development pipelines.

The main tasks of the testing environment:

- automated user interface testing
- automated API testing
- containerized runtime environment
- configuration management using YAML profiles
- integration with CI/CD
- test reporting and analysis of results

The framework is implemented using Python and modern test automation tools.

---

## Technology stack

- Python 3.12
- Pytest
- Playwright
- Docker / Docker Compose
- Allure Reports
- GitHub Actions (CI/CD)

Additional libraries:

- requests
- pyyaml

---

## Architecture

The system consists of three main components:

1. **Demo application**
2. **Framework for end-to-end testing**
3. **CI/CD documentation and configuration**

The architecture of the framework is designed to provide modularity and extensibility.

The main elements of the framework include:

- a layer of interaction with the browser
- configuration module
- the object page layer
- reusable user interface components
- automated test suites
- utilities for creating reports and logging

Project structure:

```
demo-app/
e2e-framework/
docs/
docker-compose.yml
```

---

## Demo application

The demo-app directory contains a lightweight web application used as a test system.

It includes:

- HTML interface
- simple JavaScript logic
- minimal backend server

This allows for stable and reproducible user interface and API tests.

---

## E2E Framework

The framework itself is located in the 'e2e-framework` directory.

The framework includes several functional modules responsible for various aspects of automated testing.

Main components:

### Components

Reusable user interface elements:

- buttons
- input fields

These components help simplify interaction with user interface elements and reduce code duplication.

### Core

Basic utilities such as browser initialization.

Example:

- BrowserFactory — creates and configures browser instances.

### Locators

It contains selectors used for testing the user interface.

Separate locator files are created for different applications.

### Pages

Implements the **Page Object Model (POM)** design pattern.

Each page class represents a specific web page and encapsulates the logic of interaction with the user interface.

### Tests

The test suites are divided into:

- API tests
- User interface tests

Each test group is targeted at a specific application or testing environment.

---

### Configuration system

The framework supports configuration using **YAML files and environment variables**, which allows you to flexibly switch between different testing environments.

Configuration examples:

- demoapp.local.yaml
- demoapp.docker.yaml
- demoqa.local.yaml

The configuration makes it easy to switch between environments.

### Logging and testing artifacts

During the execution of tests, the framework can collect useful artifacts such as:

- execution logs
- screenshots in case of failure
- test reports

These artifacts help analyze failed tests and improve debugging.

---

## Running tests

The tests are performed using Pytest.

Examples:

```
pytest -k api -s -m app_demoapp --config=demoapp.local.yaml
pytest -m app_demoapp --config=demoapp.local.yaml
```

---

## Integration with Docker

The test environment can be run inside Docker containers.

This approach ensures that the tests are run in a consistent and reproducible environment, regardless of the developer's local configuration.

Examples of commands: 

```
docker compose build
docker compose up -d demo-app
docker compose up e2e-demoapp
docker compose up e2e-demoqa
```

Containerization makes it easy to integrate the framework into CI/CD pipelines.

---

## Test Reports

Allure is used to generate interactive reports.

```
allure serve reports/allure-results
```

The reports include:

- test results
- timeline of execution
- logs
- attachments

---

## Continuous integration

GitHub Actions Pipeline automatically:

1. creates containers
2. Runs the tests
3. Preserves artifacts

---

## Future improvements

Possible future extensions:

- parallel execution of tests
- integration with test management systems
- automatic creation of defects
- support for performance testing
- closer connection with CI/CD systems and cloud environments
- using artificial intelligence to analyze test results
- increasing the level of autonomy of test systems

---