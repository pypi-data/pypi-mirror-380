SHELL := /bin/bash

# =============================================================================
# Configuration and Environment Variables
# =============================================================================

.DEFAULT_GOAL := help
.ONESHELL:
.EXPORT_ALL_VARIABLES:
MAKEFLAGS += --no-print-directory

# -----------------------------------------------------------------------------
# Display Formatting and Colors
# -----------------------------------------------------------------------------
BLUE := $(shell printf "\033[1;34m")
GREEN := $(shell printf "\033[1;32m")
RED := $(shell printf "\033[1;31m")
YELLOW := $(shell printf "\033[1;33m")
NC := $(shell printf "\033[0m")
INFO := $(shell printf "$(BLUE)ℹ$(NC)")
OK := $(shell printf "$(GREEN)✓$(NC)")
WARN := $(shell printf "$(YELLOW)⚠$(NC)")
ERROR := $(shell printf "$(RED)✖$(NC)")

# =============================================================================
# Help and Documentation
# =============================================================================

.PHONY: help
help:                                               ## Display this help text for Makefile
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z0-9_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

# =============================================================================
# Installation and Environment Setup
# =============================================================================

.PHONY: install-uv
install-uv:                                         ## Install latest version of uv
	@echo "${INFO} Installing uv..."
	@curl -LsSf https://astral.sh/uv/install.sh | sh >/dev/null 2>&1
	@echo "${OK} UV installed successfully"

.PHONY: install
install: clean                                      ## Install the project, dependencies, and pre-commit for local development
	@echo "${INFO} Starting fresh installation..."
	@uv python pin 3.9 >/dev/null 2>&1
	@uv sync --all-extras --dev
	@echo "${OK} Installation complete! ⚡"

.PHONY: destroy
destroy:                                            ## Destroy the virtual environment
	@echo "${INFO} Destroying virtual environment... 💥"
	@uv run pre-commit clean >/dev/null 2>&1 || true
	@rm -rf .venv
	@echo "${OK} Virtual environment destroyed 💥"

# =============================================================================
# Dependency Management
# =============================================================================

.PHONY: upgrade
upgrade:                                            ## Upgrade all dependencies to latest stable versions
	@echo "${INFO} Updating all dependencies... 🔄"
	@uv lock --upgrade
	@echo "${OK} Dependencies updated 🔄"
	@uv run pre-commit autoupdate
	@echo "${OK} Updated Pre-commit hooks 🔄"

.PHONY: lock
lock:                                               ## Rebuild lockfiles from scratch
	@echo "${INFO} Rebuilding lockfiles... 🔄"
	@uv lock --upgrade >/dev/null 2>&1
	@echo "${OK} Lockfiles updated"

# =============================================================================
# Build and Release
# =============================================================================

.PHONY: build
build:                                              ## Build the project
	@echo "${INFO} Building package... 📦"
	@uv build >/dev/null 2>&1
	@echo "${OK} Package build complete"

# =============================================================================
# Cleaning and Maintenance
# =============================================================================

.PHONY: clean
clean:                                              ## Cleanup temporary build artifacts
	@echo "${INFO} Cleaning working directory... 🧹"
	@rm -rf .pytest_cache .ruff_cache .hypothesis build/ dist/ .eggs/ .coverage coverage.xml coverage.json htmlcov/ .pytest_cache tests/.pytest_cache tests/**/.pytest_cache .mypy_cache >/dev/null 2>&1
	@find . -name '*.egg-info' -exec rm -rf {} + >/dev/null 2>&1
	@find . -type f -name '*.egg' -exec rm -f {} + >/dev/null 2>&1
	@find . -name '*.pyc' -exec rm -f {} + >/dev/null 2>&1
	@find . -name '*.pyo' -exec rm -f {} + >/dev/null 2>&1
	@find . -name '*~' -exec rm -f {} + >/dev/null 2>&1
	@find . -name '__pycache__' -exec rm -rf {} + >/dev/null 2>&1
	@find . -name '.ipynb_checkpoints' -exec rm -rf {} + >/dev/null 2>&1
	@echo "${OK} Working directory cleaned"
	$(MAKE) docs-clean

# =============================================================================
# Testing and Quality Checks
# =============================================================================

.PHONY: test
test:                                               ## Run the tests
	@echo "${INFO} Running test cases... 🧪"
	@uv run pytest tests
	@echo "${OK} Tests complete ✨"

.PHONY: test-all
test-all: test                                      ## Run all tests

.PHONY: coverage
coverage:                                           ## Run tests with coverage report
	@echo "${INFO} Running tests with coverage... 📊"
	@uv run pytest tests --cov -n auto
	@uv run coverage html >/dev/null 2>&1
	@uv run coverage xml >/dev/null 2>&1
	@echo "${OK} Coverage report generated ✨"

# -----------------------------------------------------------------------------
# Type Checking
# -----------------------------------------------------------------------------

.PHONY: mypy
mypy:                                               ## Run mypy
	@echo "${INFO} Running mypy... 🔄"
	@uv run dmypy run litestar_mcp tests || uv run mypy litestar_mcp tests
	@echo "${OK} Mypy checks passed ✨"

.PHONY: mypy-nocache
mypy-nocache:                                       ## Run Mypy without cache
	@echo "${INFO} Running mypy without cache... 🔄"
	@uv run mypy litestar_mcp tests
	@echo "${OK} Mypy checks passed ✨"

.PHONY: pyright
pyright:                                            ## Run pyright
	@echo "${INFO} Running pyright... 🔄"
	@uv run pyright litestar_mcp tests
	@echo "${OK} Pyright checks passed ✨"

.PHONY: type-check
type-check: mypy pyright                            ## Run all type checking

# -----------------------------------------------------------------------------
# Linting and Formatting
# -----------------------------------------------------------------------------

.PHONY: pre-commit
pre-commit:                                         ## Run pre-commit hooks
	@echo "${INFO} Running pre-commit checks... ="
	@uv run pre-commit run --all-files
	@echo "${OK} Pre-commit checks passed ✨"

.PHONY: ruff-check
ruff-check:                                         ## Run ruff linting
	@echo "${INFO} Running ruff checks... 🔄"
	@uv run ruff check --fix litestar_mcp tests
	@echo "${OK} Ruff checks passed ✨"

.PHONY: ruff-format
ruff-format:                                        ## Run ruff formatting
	@echo "${INFO} Running ruff formatting... 🎨"
	@uv run ruff format litestar_mcp tests
	@echo "${OK} Ruff formatting complete ✨"

.PHONY: slotscheck
slotscheck:                                         ## Run slotscheck
	@echo "${INFO} Running slots check... 🔄"
	@uv run slotscheck litestar_mcp
	@echo "${OK} Slots check passed ✨"

.PHONY: lint
lint: ruff-check ruff-format type-check slotscheck  ## Run all linting checks

.PHONY: check-all
check-all: lint test-all coverage                   ## Run all checks (lint, test, coverage)

# =============================================================================
# Documentation
# =============================================================================

.PHONY: docs-clean
docs-clean:                                         ## Clean documentation build
	@echo "${INFO} Cleaning documentation build assets... 🧹"
	@rm -rf docs/_build >/dev/null 2>&1
	@echo "${OK} Documentation assets cleaned"

.PHONY: docs-serve
docs-serve: docs-clean                              ## Serve documentation locally
	@echo "${INFO} Starting documentation server... 📚"
	uv run sphinx-autobuild docs docs/_build/ -j auto --watch litestar_mcp --watch docs --watch tests --watch CONTRIBUTING.rst --port 8002

.PHONY: docs
docs: docs-clean                                    ## Build documentation
	@echo "${INFO} Building documentation... 📚"
	@uv run sphinx-build -M html docs docs/_build/ -E -a -j auto -W --keep-going
	@echo "${OK} Documentation built successfully"

.PHONY: docs-linkcheck
docs-linkcheck:                                     ## Check documentation links
	@echo "${INFO} Checking documentation links... 🔗"
	@uv run sphinx-build -b linkcheck ./docs ./docs/_build -D linkcheck_ignore='http://.*','https://.*'
	@echo "${OK} Link check complete"

.PHONY: docs-linkcheck-full
docs-linkcheck-full:                                ## Run full documentation link check
	@echo "${INFO} Running full link check... 🔗"
	@uv run sphinx-build -b linkcheck ./docs ./docs/_build -D linkcheck_anchors=0
	@echo "${OK} Full link check complete"

# =============================================================================
# MCP Specific Targets
# =============================================================================

.PHONY: mcp-test
mcp-test:                                           ## Run MCP protocol tests specifically
	@echo "${INFO} Running MCP protocol tests... 🔌"
	@uv run pytest tests -m "not slow" -k "mcp" -v
	@echo "${OK} MCP tests complete ✨"

.PHONY: websocket-test
websocket-test:                                     ## Run WebSocket handler tests
	@echo "${INFO} Running WebSocket tests... 🔌"
	@uv run pytest tests -k "websocket" -v
	@echo "${OK} WebSocket tests complete ✨"

.PHONY: integration-test
integration-test:                                   ## Run integration tests
	@echo "${INFO} Running integration tests... 🔗"
	@uv run pytest tests/integration/ -v
	@echo "${OK} Integration tests complete ✨"

.PHONY: example-run
example-run:                                        ## Run basic example
	@echo "${INFO} Running basic example... 🚀"
	@uv run python examples/basic_usage.py
	@echo "${OK} Example completed ✨"

# =============================================================================
# Development Targets
# =============================================================================

.PHONY: dev-setup
dev-setup: install lint test                       ## Complete development setup
	@echo "${OK} Development environment ready! 🚀"

.PHONY: quick-test
quick-test:                                         ## Run quick tests (no coverage)
	@echo "${INFO} Running quick tests... ⚡"
	@uv run pytest tests -x --ff
	@echo "${OK} Quick tests complete ✨"

.PHONY: watch-test
watch-test:                                         ## Run tests in watch mode
	@echo "${INFO} Running tests in watch mode... 👀"
	@uv run pytest-watch tests

.PHONY: format-check
format-check:                                       ## Check if code is formatted correctly
	@echo "${INFO} Checking code formatting... 🔍"
	@uv run ruff format --check litestar_mcp tests
	@echo "${OK} Code formatting check complete ✨"
