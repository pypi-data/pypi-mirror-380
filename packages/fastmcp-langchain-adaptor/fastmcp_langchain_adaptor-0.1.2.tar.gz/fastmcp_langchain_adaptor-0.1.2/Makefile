# Makefile for fastmcp-langchain-adaptor

.PHONY: help install install-dev test test-cov lint format type-check security clean build publish docs serve-docs

help:	## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-15s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install:	## Install the package
	uv sync

install-dev:	## Install in development mode with all dependencies
	uv sync --dev
	uv run pre-commit install

test:	## Run tests
	uv run pytest

test-cov:	## Run tests with coverage report
	uv run pytest --cov=fastmcp_langchain_adaptor --cov-report=html --cov-report=term

lint:	## Run linting (ruff)
	uv run ruff check .

format:	## Format code (black + ruff fixes)
	uv run black .
	uv run ruff check . --fix

type-check:	## Run type checking (mypy)
	uv run mypy fastmcp_langchain_adaptor/

security:	## Run security checks (bandit + safety)
	uv run bandit -r fastmcp_langchain_adaptor/
	uv run safety check

clean:	## Clean build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf .ruff_cache/
	rm -rf htmlcov/
	find . -type d -name __pycache__ -delete
	find . -type f -name "*.pyc" -delete

build:	## Build package
	uv build

publish-test:	## Publish to TestPyPI
	uv publish --repository testpypi

publish:	## Publish to PyPI
	uv publish

docs:	## Build documentation
	uv run mkdocs build

serve-docs:	## Serve documentation locally
	uv run mkdocs serve

pre-commit:	## Run all pre-commit hooks
	uv run pre-commit run --all-files

check-all:	## Run all checks (test, lint, type-check, security)
	make test
	make lint
	make type-check
	make security

ci:	## Run CI checks (for GitHub Actions)
	make install-dev
	make check-all
