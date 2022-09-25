# Solution for Wundernut coding challenge Vol.12

## Requirements

- Python 3.10.6
- Dependency management: Poetry ~1.2.0
    - https://python-poetry.org/docs/#installation

### Optional

- GNU Make

## Running the solution

### With GNU Make

1. Run `make run`

### Manually

Run all commands in the project folder.

1. Install the dependencies: `poetry install`
2. Run the script: `poetry run python main.py`
3. The output will include:
    - The extracted text from the image
    - The decrypted text
    - The decrypted text auto-segmented into a more human-readable format
