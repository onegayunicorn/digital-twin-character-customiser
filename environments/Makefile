# Aether Core — Makefile (run environments)
.PHONY: help install dev build preview test typecheck sim sim-all pipeline docker-build docker-up docker-down hooks lint

help: ## Show available targets
	@grep -E '^[a-zA-Z_-]+:.*## ' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*## "}; {printf "  \033[36m%-14s\033[0m %s\n", $$1, $$2}'

install: ## Install all workspace dependencies
	npm install --no-audit --no-fund

dev: ## Start the Vite dev server
	npm run dev

build: ## Production build of the web-app
	npm run build

preview: ## Preview the production build
	npm run preview

test: ## Run all Vitest suites
	npm test

typecheck: ## TypeScript check across all packages
	npm run typecheck

sim: ## Run all simulations
	npm run sim:all

sim-lifestyle: ## Lifestyle hour-allocation simulation
	npm run sim:lifestyle

sim-agent-matrix: ## Agent matrix evolution simulation
	npm run sim:agent-matrix

sim-telemetry: ## Schumann telemetry stream simulation
	npm run sim:telemetry

sim-quantum: ## Quantum Reality Interface simulation
	npm run sim:quantum

pipeline: ## Run the data pipelines
	npm run pipeline:telemetry && npm run pipeline:manifest && npm run pipeline:sync

docker-build: ## Build web + api images
	docker compose -f environments/docker-compose.yml build

docker-up: ## Start the full stack (web + api + mysql)
	docker compose -f environments/docker-compose.yml up -d

docker-down: ## Stop the stack
	docker compose -f environments/docker-compose.yml down

hooks: ## Install git hooks
	npm run hooks:install

lint: ## Alias for typecheck
	npm run typecheck
