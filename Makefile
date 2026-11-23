VENV   := .venv
PY     := $(VENV)/bin/python
PIP    := $(VENV)/bin/pip
RUFF   := $(VENV)/bin/ruff
MYPY   := $(VENV)/bin/mypy
PYTEST := $(VENV)/bin/pytest

.PHONY: help setup lint format test run clean dev-fastapi

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "%-14s %s\n", $$1, $$2}'

setup: ## Create venv and install deps (editable, with dev extras)
	$(PY) -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -e ".[dev]"

lint: ## Run ruff + mypy
	$(RUFF) check .
	@if find . -name '*.py' -not -path './$(VENV)/*' -not -path './.git/*' | grep -q .; then \
		$(MYPY) .; \
	else \
		echo "mypy: no Python files yet, skipping"; \
	fi

format: ## Format with ruff
	$(RUFF) format .

test: ## Run pytest (ignore exit code 5 = "no tests collected")
	$(PYTEST) || [ $$? -eq 5 ]

run: ## Run the target configured in run.py
	$(PY) run.py

clean: ## Remove caches
	rm -rf .ruff_cache .mypy_cache .pytest_cache
	find . -type d -name __pycache__ -prune -exec rm -rf {} +

dev-fastapi: ## Run the fastapi-fundamentals dev server
	$(VENV)/bin/fastapi dev ./03-web/fastapi/fastapi-fundamentals/src/fastapi_fundamentals/main.py
