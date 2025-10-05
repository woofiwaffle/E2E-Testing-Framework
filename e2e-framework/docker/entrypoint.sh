#!/bin/bash
echo "=== Starting E2E tests ==="
pytest -v --alluredir=reports/allure
