# Dockerfile for Flask App using Python 3.10 and Poetry
FROM python:3.10-slim as builder

WORKDIR /app

RUN pip install poetry

COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

COPY . /app

CMD ["poetry", "run", "flask", "run", "--host=0.0.0.0"]
