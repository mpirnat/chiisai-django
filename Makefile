.DEFAULT_GOAL := build

install: # Install dependencies
	poetry install

fmt format: # Run code formatters
	poetry run ruff check --select I --fix-only chiisai
	poetry run black .

lint: # Run code linters
	poetry run black --check --diff --color .
	poetry run ruff check --select E,W,F,I,S,B --show-source chiisai
	poetry run mypy --strict chiisai

test: # Run tests
	poetry run pytest chiisai

cov test-cov: # Run tests with coverage
	poetry run pytest --cov=chiisai --cov-report=term-missing --cov-report=xml -v chiisai

build: # Build project
	make install
	make lint
	make cov
