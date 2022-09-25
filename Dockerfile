# x86 Python environment for cross platform usage
FROM --platform=linux/amd64 python:3.10.6 as python-base
ENV PYTHONUNBUFFERED=True

# Install poetry
RUN pip install poetry==1.2.0

# Copy project files
COPY . /app
WORKDIR /app

# Dependencies
RUN poetry install --sync

## Preload OCR models
RUN poetry run python -c "from easyocr import Reader; Reader(lang_list=['en']);"

# This will now start Python from the .venv
CMD ["poetry", "run", "python", "./main.py"]
