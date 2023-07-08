.DEFAULT_GOAL := build

install: # Install dependencies
	poetry install

fmt format: # Run code formatters
	poetry run ruff check --select I --fix-only chiisai_django
	poetry run black .

lint: # Run code linters
	poetry run black --check --diff --color .
	poetry run ruff check --select E,W,F,I,S,B --show-source chiisai_django
	poetry run mypy --strict chiisai_django

test: # Run tests
	poetry run pytest chiisai_django

cov test-cov: # Run tests with coverage
	poetry run pytest --cov=chiisai_django --cov-report=term-missing --cov-report=xml -v chiisai_django

build: # Build project
	make install
	make lint
	make cov
