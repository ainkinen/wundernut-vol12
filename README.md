# Solution for Wundernut coding challenge Vol.12

## Requirements

- Python 3.10.6
- Poetry ~1.2.0
    - For dependency management
    - https://python-poetry.org/docs/#installation
- GNU Make

Or

- Docker

## Running the solution

Locally: `make run`  
With Docker: `make docker-build`

The output will include:

- The extracted text from the image
- The decrypted text
- The decrypted text auto-segmented into a more human-readable format
