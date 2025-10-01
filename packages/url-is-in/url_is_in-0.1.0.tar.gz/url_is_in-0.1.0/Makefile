.PHONY: install test lint clean lint-check pre-commit-install help

# Default target
help:
	@echo "Available targets:"
	@echo "  install           Install the package and dependencies using uv"
	@echo "  test              Run unit tests with pytest"
	@echo "  lint-check        Run ruff linting"
	@echo "  lint              Format code with ruff"
	@echo "  pre-commit-install Install pre-commit hooks"
	@echo "  clean             Clean up build artifacts and cache files"
	@echo "  help              Show this help message"

# Install package and dependencies
install:  # uv sync --dev
	pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit-install:
	pre-commit install

# Run tests
test:
	pytest tests/ --cov=src --cov-fail-under=95 -v

# Run linting
lint-check:
	ruff check src/ tests/

# Format code
lint:
	ruff format src/ tests/
	ruff check --fix src/ tests/

# Clean up
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".ruff_cache" -exec rm -rf {} + 2>/dev/null || true
	rm -rf build/ dist/