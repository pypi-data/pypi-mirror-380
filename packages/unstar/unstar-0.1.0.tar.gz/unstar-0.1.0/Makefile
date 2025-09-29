.PHONY: help install test lint format build clean publish-test publish

help:  ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install:  ## Install dependencies
	uv sync

test:  ## Run tests
	uv run pytest tests/ -v

lint:  ## Run linting
	uv run ruff check src/ tests/

format:  ## Format code
	uv run ruff check --fix src/ tests/
	uv run ruff format src/ tests/

build:  ## Build the package
	uv build

clean:  ## Clean build artifacts
	rm -rf dist/
	rm -rf src/*.egg-info/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

publish-test:  ## Publish to Test PyPI
	uv publish --publish-url https://test.pypi.org/legacy/

publish:  ## Publish to PyPI
	uv publish

dev-setup: install  ## Setup development environment
	@echo "Development environment setup complete!"
	@echo "Run 'make help' to see available commands"

check: lint test  ## Run all checks (lint + test)

all: clean format check build  ## Run full pipeline