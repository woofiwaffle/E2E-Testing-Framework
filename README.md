# E2E Testing Framework (MVP)

Минимальный рабочий пример E2E-фреймворка с Playwright + Pytest.


Разработка фреймворка для сквозного (E2E) тестирования веб-приложений с использованием технологии контейнеризации

docker compose -f docker-compose.yml build

docker compose -f docker-compose.yml up

allure serve reports/allure-results
pytest -k api -s
pytest -m app_demoapp --config=demoapp.local.yaml
pytest -m app_demoqa --config=demoqa.local.yaml
docker compose down -v --remove-orphans
docker compose build --no-cache
docker compose up
docker compose up -d demo-app
docker compose up e2e-demoapp
docker compose up e2e-demoqa


Основные тесты писать на локальном demo-app → стабильные тесты, CI/CD, Allure отчеты.

Дополнительно продемонстрировать тесты на внешнем веб-приложении → показать, что фреймворк может работать с любыми веб-приложениями.

В документации отметить, что твой фреймворк универсален и подходит для любых веб-приложений благодаря PageFactory + компонентам + настройкам через конфиг.