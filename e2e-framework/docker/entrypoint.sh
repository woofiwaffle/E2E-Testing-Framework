#!/bin/bash
set -e
echo "=== Starting E2E tests ==="

REPORTS_DIR=${REPORTS_DIR:-/app/reports}

mkdir -p "${REPORTS_DIR}"

pytest -v

EXIT_CODE=$?
echo "=== Tests finished with exit code ${EXIT_CODE} ==="
exit ${EXIT_CODE}