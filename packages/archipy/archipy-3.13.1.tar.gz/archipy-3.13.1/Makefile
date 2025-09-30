# Variables
PYTHON := uv run
UV := uv
PRE_COMMIT := uv run pre-commit
PROJECT_NAME := archipy
PYTHON_FILES := $(PROJECT_NAME) features/steps scripts

# Colors for terminal output
BLUE := \033[1;34m
GREEN := \033[1;32m
RED := \033[1;31m
YELLOW := \033[1;33m
NC := \033[0m # No Color

.PHONY: help
help: ## Show this help message
	@echo 'Usage:'
	@echo "${BLUE}make${NC} ${GREEN}<target>${NC}"
	@echo ''
	@echo 'Targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z\-_0-9]+:.*?## / {printf "  ${BLUE}%-20s${NC} %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.PHONY: setup
setup: ## Setup project pre-requisites
	@echo "${BLUE}Setup project pre-requisites...${NC}"
	@echo "${GREEN}Installing uv (may need your sudo password)...${NC}"
	sudo apt install pipx
	pipx install uv
	pipx ensurepath
	uv generate-shell-completion bash >> ~/.bash_completion

.PHONY: install
install: ## Install project dependencies
	@echo "${BLUE}Installing project dependencies...${NC}"
	$(UV) sync --extra dev
	$(PRE_COMMIT) install

.PHONY: install-dev
install-dev: ## Install project dependencies with dev extras
	@echo "${BLUE}Installing project dependencies with dev extras...${NC}"
	$(UV) sync --all-extras --all-groups
	$(PRE_COMMIT) install

.PHONY: update
update: ## Update dependencies to their latest versions
	@echo "${BLUE}Updating dependencies...${NC}"
	$(UV) lock --upgrade

.PHONY: clean
clean: ## Remove build artifacts and cache directories
	@echo "${BLUE}Cleaning project...${NC}"
	rm -rf dist/
	rm -rf build/
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf .mypy_cache/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

.PHONY: format
format: ## Format code using black
	@echo "${BLUE}Formatting code...${NC}"
	$(PYTHON) black --config pyproject.toml $(PYTHON_FILES)

.PHONY: lint
lint: ## Run all linters
	@echo "${BLUE}Running linters...${NC}"
	$(PYTHON) ruff check --config pyproject.toml  $(PYTHON_FILES)
	$(PYTHON) mypy --config-file pyproject.toml $(PYTHON_FILES)

.PHONY: security
security: ## Run security scan with Bandit
	@echo "${BLUE}Running security scan...${NC}"
	$(PYTHON) bandit -c pyproject.toml -r archipy/ -f json -o bandit-report.json || true

.PHONY: behave
behave: ## Run tests with behave
	@echo "${BLUE}Running tests...${NC}"
	$(UV) run --extra behave behave

.PHONY: test
test: behave ## Run tests (alias for behave)

.PHONY: build
build: clean ## Build project distribution
	@echo "${BLUE}Building project distribution...${NC}"
	$(UV) build

.PHONY: version
version: ## Display current version
	@echo "${BLUE}Current version:${NC}"
	@$(UV) run python -c "import tomllib; print(f\"archipy {tomllib.load(open('pyproject.toml', 'rb'))['project']['version']}\")"
	@echo "${YELLOW}Current tag:${NC}"
	@git describe --tags --abbrev=0 2>/dev/null || echo "No tags found"

.PHONY: bump-patch
bump-patch: ## Bump patch version
	@echo "${BLUE}Bumping patch version...${NC}"
	@if [ -n "$(message)" ]; then \
		$(UV) run python scripts/bump_version.py patch -m "$(message)"; \
	else \
		$(UV) run python scripts/bump_version.py patch -m "$$(git log -1 --pretty=%s)"; \
	fi

.PHONY: bump-minor
bump-minor: ## Bump minor version
	@echo "${BLUE}Bumping minor version...${NC}"
	@if [ -n "$(message)" ]; then \
		$(UV) run python scripts/bump_version.py minor -m "$(message)"; \
	else \
		$(UV) run python scripts/bump_version.py minor -m "$$(git log -1 --pretty=%s)"; \
	fi

.PHONY: bump-major
bump-major: ## Bump major version
	@echo "${BLUE}Bumping major version...${NC}"
	@if [ -n "$(message)" ]; then \
		$(UV) run python scripts/bump_version.py major -m "$(message)"; \
	else \
		$(UV) run python scripts/bump_version.py major -m "$$(git log -1 --pretty=%s)"; \
	fi

.PHONY: docker-build
docker-build: ## Build Docker image
	@echo "${BLUE}Building Docker image...${NC}"
	docker build -t $(PROJECT_NAME) .

.PHONY: docker-run
docker-run: ## Run Docker container
	@echo "${BLUE}Running Docker container...${NC}"
	docker run -it --rm $(PROJECT_NAME)

.PHONY: pre-commit
pre-commit: ## Run pre-commit hooks
	@echo "${BLUE}Running pre-commit hooks...${NC}"
	$(PRE_COMMIT) run --all-files

.PHONY: check
check: lint security behave ## Run all checks (linting, security, and tests)

.PHONY: ci
ci: ## Run CI pipeline locally
	@echo "${BLUE}Running CI pipeline...${NC}"
	$(MAKE) clean
	$(MAKE) install-dev
	$(MAKE) lint
	$(MAKE) security
	$(MAKE) behave
	$(MAKE) build

.PHONY: docs-serve
docs-serve: ## Serve MkDocs documentation locally
	@echo "${BLUE}Serving documentation...${NC}"
	$(UV) run --group docs mkdocs serve

.PHONY: docs-build
docs-build: ## Build MkDocs documentation
	@echo "${BLUE}Building documentation...${NC}"
	$(UV) run --group docs mkdocs build

.PHONY: docs-deploy
docs-deploy: ## Deploy MkDocs to GitHub Pages
	@echo "${BLUE}Deploying documentation...${NC}"
	$(UV) run --group docs mkdocs gh-deploy --force

.DEFAULT_GOAL := help
