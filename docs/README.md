## Фреймворк для сквозного тестирования — Документация проекта

### Введение

Этот проект реализует фреймворк для автоматизированного тестирования веб-приложений.

Основная цель проекта — разработка многократно используемого фреймворка, поддерживающего:

- автоматизированное тестирование пользовательского интерфейса
- автоматизированное тестирование API
- контейнеризированное выполнение
- интеграцию с CI/CD
- отчеты о тестировании

Фреймворк реализован с использованием Python и современных инструментов автоматизации тестирования.

---

## Технологический стек

- Python 3.12
- Pytest
- Playwright
- Docker / Docker Compose
- Allure Reports
- GitHub Actions (CI/CD)

Дополнительные библиотеки:

- requests
- pyyaml

---

## Архитектура

Система состоит из трех основных компонентов:

1. **Демонстрационное приложение**
2. **Фреймворк для сквозного тестирования**
3. **Документация и конфигурация CI/CD**

Структура проекта:

```
demo-app/
e2e-framework/
docs/
docker-compose.yml
```

---

## Демо-приложение

В каталоге `demo-app` находится легковесное веб-приложение, используемое в качестве тестируемой системы.

Оно включает в себя:

- HTML-интерфейс
- простую логику на JavaScript
- минимальный бэкэнд-сервер

Это позволяет проводить стабильные и воспроизводимые тесты пользовательского интерфейса и API.

---

## E2E Framework

Сам фреймворк находится в каталоге `e2e-framework`.

Основные компоненты:

### Компоненты

Повторно используемые элементы пользовательского интерфейса:

- кнопки
- поля ввода

### Ядро

Основные утилиты, такие как инициализация браузера.

Пример:

- BrowserFactory

### Локаторы

Содержит селекторы, используемые для тестирования пользовательского интерфейса.

Для разных приложений создаются отдельные файлы локаторов.

### Страницы

Реализует шаблон проектирования **Page Object Model**.

Каждый класс страницы представляет собой конкретную веб-страницу.

### Тесты

Наборы тестов разделены на:

- API-тесты
- Тесты пользовательского интерфейса

Каждая группа тестов нацелена на конкретное приложение.

---

## Система конфигурации

Конфигурация фреймворка хранится в файлах YAML.

Примеры конфигураций:

- demoapp.local.yaml
- demoapp.docker.yaml
- demoqa.local.yaml

Конфигурация позволяет легко переключаться между средами.

---

## Выполнение тестов

Тесты выполняются с помощью Pytest.

Примеры:

```
pytest
pytest -k api
pytest -m app_demoapp --config=demoapp.local.yaml
```

---

## Интеграция с Docker

Всю среду можно запустить с помощью Docker.

```
docker compose build
docker compose up -d demo-app
docker compose up e2e-demoapp
docker compose up e2e-demoqa
```

Это обеспечивает одинаковую среду для всех разработчиков и конвейеров CI.

---

## Отчеты о тестировании

Allure используется для генерации интерактивных отчетов.

```
allure serve reports/allure-results
```

Отчеты включают:

- результаты тестов
- временную шкалу выполнения
- логи
- вложения

---

## Непрерывная интеграция

Конвейер GitHub Actions автоматически:

1. создает контейнеры
2. запускает тесты
3. сохраняет артефакты

---

## Будущие улучшения

Возможные будущие расширения:

- параллельное выполнение тестов
- интеграция с системами управления тестированием
- автоматическое создание дефектов
- поддержка тестирования производительности

---
---
---

## E2E Testing Framework — Project Documentation

### Introduction

This project implements an automated testing framework for web applications.

The main goal of the project is to design a reusable framework that supports:

- automated UI testing
- automated API testing
- containerized execution
- CI/CD integration
- test reporting

The framework is implemented using Python and modern test automation tools.

---

## Technology Stack

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

## Demo Application

The `demo-app` directory contains a lightweight web application used as the system under test.

It includes:

- HTML interface
- simple JavaScript logic
- minimal backend server

This allows stable and reproducible UI and API tests.

---

## E2E Framework

The framework itself is located in the `e2e-framework` directory.

Main components:

### Components

Reusable UI elements:

- buttons
- inputs

### Core

Core utilities such as browser initialization.

Example:

- BrowserFactory

### Locators

Contains selectors used for UI testing.

Separate locator files are created for different applications.

### Pages

Implements **Page Object Model** design pattern.

Each page class represents a specific web page.

### Tests

Test suites divided into:

- API tests
- UI tests

Each test group targets a specific application.

---

## Configuration System

Framework configuration is stored in YAML files.

Example configurations:

- demoapp.local.yaml
- demoapp.docker.yaml
- demoqa.local.yaml

Configuration allows switching environments easily.

---

## Test Execution

Tests are executed using Pytest.

Examples:

```
pytest
pytest -k api
pytest -m app_demoapp --config=demoapp.local.yaml
```

---

## Docker Integration

The entire environment can be started using Docker.

```
docker compose build
docker compose up -d demo-app
docker compose up e2e-demoapp
docker compose up e2e-demoqa
```

This ensures the same environment for all developers and CI pipelines.

---

## Test Reports

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

## Continuous Integration

GitHub Actions pipeline automatically:

1. builds containers
2. runs tests
3. stores artifacts

---

## Future Improvements

Possible future extensions:

- parallel test execution
- integration with test management systems
- automatic defect creation
- performance testing support