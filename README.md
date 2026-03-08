## E2E Testing Framework (Фреймворк для сквозного тестирования веб-приложений)

Фреймворк для сквозного (E2E) тестирования веб-приложений с использованием контейнеризации.

Проект демонстрирует, как можно выполнять автоматизированные тесты браузера и API в воспроизводимой среде с помощью Docker, Playwright, Pytest и системы отчетности Allure.

---

### Обзор проекта

Репозиторий содержит:

- **demo-app** — простое веб-приложение, используемое в качестве тестируемой системы (SUT)
- **e2e-framework** — фреймворк для автоматизированного тестирования пользовательского интерфейса и API
- **docker-compose** — контейнеризированная среда для запуска приложения и тестов
- **GitHub Actions CI/CD** — автоматизированное выполнение тестов в конвейере
- **Allure reports** — визуальные отчеты о выполнении тестов

Фреймворк разработан как **универсальный**, то есть его можно адаптировать для тестирования различных веб-приложений путем настройки локаторов, объектов страниц и параметров среды.

---

## Быстрый старт

### Сборка контейнеров Docker

```bash
docker compose -f docker-compose.yml build
```

### Запуск среды для DemoApp

```bash
docker compose up -d demo-app

docker compose up e2e-demoapp
```

Эта команда запускает:

- демонстрационное приложение
- контейнер для запуска сквозных тестов для DemoApp

### Запуск среды для DemoQA

```bash
docker compose up e2e-demoqa
```

Эта команда запускает:
- контейнер для запуска скзвонхы тестов для внешнего веб-приложения DemoQA

---

## Запуск тестов вручную (Примеры)

Активация виртуальной среды (Windows PowerShell):

```bash
. .\.venv\Scripts\Activate.ps1
```

Запуск только тестов API для DemoApp:

```bash
pytest -k api -s -m app_demoapp --config=demoapp.local.yaml
```

Запуск только тестов UI для DemoApp:
```bash
pytest -k ui -s -m app_demoapp --config=demoapp.local.yaml
```

Запуск тестов DemoApp:

```bash
pytest -m app_demoapp --config=demoapp.local.yaml
```

Запуск тестов DemoQA:

```bash
pytest -m app_demoqa --config=demoqa.local.yaml
```

---

## Отчет Allure

Перед использованием Allure убедитесь:

- Java установлена
- Allure CLI доступен в PATH

Сгенерируйте и откройте отчет:

```bash
allure serve reports/allure-results
```

---

## Команды Docker

Остановка Окружение:

```bash
docker compose down -v --remove-orphans
```

Пересборка образов без кэша:

```bash
docker compose build --no-cache
```

---

## Примечания

Основной набор тестов выполняется на **локальном демонстрационном приложении**, что обеспечивает стабильную и воспроизводимую среду тестирования.

Дополнительно фреймворк демонстрируется на **внешнем веб-приложении DemoQA**, чтобы показать возможность применения разработанного решения для тестирования сторонних веб-систем без изменения архитектуры фреймворка.

Такой подход демонстрирует универсальность и переносимость разработанного тестового фреймворка.

---
---
---

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