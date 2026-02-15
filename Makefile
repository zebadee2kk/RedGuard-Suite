.PHONY: install install-dev lint format typecheck test test-cov check security clean help

PYTHON ?= python3
SRC_DIR = src
TEST_DIR = tests

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install package in production mode
	$(PYTHON) -m pip install .

install-dev: ## Install package with dev dependencies
	$(PYTHON) -m pip install -e ".[dev]"
	pre-commit install

lint: ## Run ruff linter
	ruff check $(SRC_DIR) $(TEST_DIR)

format: ## Auto-format code with ruff
	ruff format $(SRC_DIR) $(TEST_DIR)
	ruff check --fix $(SRC_DIR) $(TEST_DIR)

typecheck: ## Run mypy type checker
	mypy $(SRC_DIR)

test: ## Run tests
	pytest $(TEST_DIR)

test-cov: ## Run tests with coverage report
	pytest $(TEST_DIR) --cov=redguard --cov-report=term-missing --cov-report=html

check: lint typecheck test ## Run all checks (lint + typecheck + test)

security: ## Run security checks (bandit + detect-secrets)
	bandit -r $(SRC_DIR) -c pyproject.toml
	@echo "Security scan complete."

clean: ## Remove build artifacts
	rm -rf build/ dist/ *.egg-info .pytest_cache .mypy_cache .ruff_cache htmlcov .coverage
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true

docker-build: ## Build Docker image
	docker build -t redguard-suite:dev -f docker/Dockerfile .

docker-run: ## Run RedGuard in Docker
	docker run --rm -it redguard-suite:dev
