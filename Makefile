.PHONY: install run

install:
	@poetry install --sync

run: install
	@poetry run python main.py
