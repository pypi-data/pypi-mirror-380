.PHONY: help install generate lint lint-fix test test-cov test-unit test-integration test-functional

# Default target - auto-generate help from comments
help: ## Show available commands
	@echo "📋 Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*##' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*##"}; {printf "  make %-10s - %s\n", $$1, $$2}'
	

install: ## Install init_mater_project package in editable mode
	uv pip install -e .


generate: ## Generate a MATER sample project locally 
	@rm -rf local-project
	uv run init-mater-project local-project
	@echo "\n✓ Local sample project generated\n"


lint: ## Run code linting and formatting checks
	@echo "Linting and formatting checks...\n"
	@uv run ruff check . || echo "❌ Linting issues found"
	@uv run ruff format --check . || echo "❌ Formatting issues found"
	@echo "\n📋 Lint checks completed"


lint-fix: ## Fix linting issues automatically  
	@echo "Fixing linting and formatting issues...\n"
	@uv run ruff check . --fix || echo "⚠️ Some issues require manual fixing"
	@uv run ruff format . || echo "❌ Formatting failed"
	@echo "\n📋 Lint fixes completed"


test: ## Run tests with verbose output
	@echo "🧪 Running tests..."
	@echo ""
	uv sync --group test
	@echo ""
	uv run pytest -v --tb=short


test-cov: ## Run tests with coverage report
	@echo "📊 Running tests with coverage..."
	@echo ""
	uv sync --group test
	@echo ""
	uv run pytest -v --tb=short --cov=src/init_mater_project --cov-report=term-missing


test-unit: ## Run unit tests with verbose output
	@echo "⚡ Running unit tests..."
	@echo ""
	uv sync --group test
	@echo ""
	uv run pytest tests/unit/ -v --tb=short


test-integration: ## Run integration tests with verbose output
	@echo "🔗 Running integration tests..."
	@echo ""
	uv sync --group test
	@echo ""
	uv run pytest tests/integration/ -v --tb=short


test-functional: ## Run functional tests with verbose output
	@echo "🎯 Running functional tests..."
	@echo ""
	uv sync --group test
	@echo ""
	uv run pytest tests/functional/ -v --tb=short