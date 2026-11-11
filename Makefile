.PHONY: help setup lint format test clean

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "%-10s %s\n", $$1, $$2}'

setup: ## Create venv and install deps
	python -m venv .venv
	. .venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt -r requirements-dev.txt

lint: ## Run ruff + mypy
	ruff check .
	@if find . -name '*.py' -not -path './.venv/*' -not -path './.git/*' | grep -q .; then mypy .; else echo "mypy: no Python files yet, skipping"; fi

format: ## Format with ruff
	ruff format .

test: ## Run pytest
	pytest || [ $$? -eq 5 ]

clean: ## Remove caches
	rm -rf .ruff_cache .mypy_cache .pytest_cache
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
