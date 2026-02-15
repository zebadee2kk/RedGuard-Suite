#!/usr/bin/env bash
# Run all quality checks locally (equivalent to CI pipeline).
# Usage: ./scripts/run_checks.sh
set -euo pipefail

echo "=== Ruff Lint ==="
ruff check src/ tests/

echo "=== Ruff Format ==="
ruff format --check src/ tests/

echo "=== Pytest ==="
pytest tests/ --cov=redguard --cov-report=term-missing --cov-fail-under=80

echo "=== Bandit ==="
bandit -r src/ -c pyproject.toml

echo "=== All checks passed ==="
