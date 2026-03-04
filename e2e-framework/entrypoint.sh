#!/bin/bash
set -e

ALLURE_RESULTS_DIR=/app/reports/allure-results

mkdir -p "$ALLURE_RESULTS_DIR"
rm -rf "$ALLURE_RESULTS_DIR"/*

if [ "$SKIP_WAIT" != "1" ]; then
  echo "Waiting for demo-app..."
  until curl -s http://demo-app:3000/healthz > /dev/null; do
    sleep 1
  done
  echo "demo-app is ready"
else
  echo "SKIP_WAIT enabled, skipping demo-app wait"
fi

echo "Running pytest with Allure..."

pytest -m "${PYTEST_MARK}" --alluredir="$ALLURE_RESULTS_DIR" --config="${CONFIG_FILE}"