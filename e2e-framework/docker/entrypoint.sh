#!/bin/bash
set -e
echo "=== Starting E2E tests ==="

REPORTS_DIR=${REPORTS_DIR:-reports/allure-results}

mkdir -p "${REPORTS_DIR}"

pytest -v --alluredir="${REPORTS_DIR}"
exit $?