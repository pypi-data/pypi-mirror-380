.PHONY: help install install-dev lint format type-check test build clean

help:
	@echo "Available commands:"
	@echo "  make install      - Install package"
	@echo "  make install-dev  - Install package with dev dependencies"
	@echo "  make lint         - Run ruff linter"
	@echo "  make format       - Format code with black"
	@echo "  make format-check - Check code formatting without modifying"
	@echo "  make type-check   - Run mypy type checker"
	@echo "  make test         - Run tests"
	@echo "  make build        - Build package"
	@echo "  make clean        - Clean build artifacts"
	@echo "  make all          - Run linting, formatting check, type check, and build"

install:
	pip install -e .

install-dev:
	pip install -e ".[dev]"
	pip install pre-commit
	pre-commit install

lint:
	ruff check corecli/

lint-fix:
	ruff check --fix corecli/

format:
	black corecli/

format-check:
	black --check corecli/

type-check:
	mypy corecli/

test:
	pytest tests/ -v

build:
	python -m build
	twine check dist/*

clean:
	rm -rf dist/ build/ *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name '*.pyc' -delete

all: lint format-check type-check build
	@echo "✅ All checks passed!"
