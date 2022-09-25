.PHONY: install run lint type-check docker-build docker-run docker-shell

install:
	@poetry install --sync

run: install
	@poetry run python main.py

lint: install
	@poetry run flake8

type-check: install
	@poetry run mypy .

docker-build:
	@docker build -t wundernut:latest .

docker-run: docker-build
	@docker run wundernut:latest

docker-shell: docker-build
	@docker run -it --entrypoint /bin/bash wundernut:latest
