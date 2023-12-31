.DEFAULT_GOAL := build

install: # Install dependencies
	poetry install

fmt format: # Run code formatters
	poetry run ruff check --select I --fix-only chiisai
	poetry run black .

lint: # Run code linters
	poetry run black --check --diff --color .
	poetry run ruff check --show-source chiisai
	poetry run mypy --strict chiisai

test: # Run tests
	poetry run pytest chiisai

cov test-cov: # Run tests with coverage
	poetry run pytest --cov=chiisai --cov-report=term-missing --cov-report=xml -v chiisai

migrate: # Run django migrations
	poetry run python chiisai/manage.py migrate

build: # Build project
	make install
	make lint
	make cov
	make migrate

requirements: # Refresh requirements.txt
	poetry export -f requirements.txt --output requirements.txt

runserver: # Run django locally
	poetry run python chiisai/manage.py runserver
