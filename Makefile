.PHONY: install run lint type-check

install:
	@poetry install --sync

run: install
	@poetry run python main.py

lint: install
	@poetry run flake8

type-check: install
	@poetry run mypy .
