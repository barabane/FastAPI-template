FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app/
COPY pyproject.toml poetry.lock ./

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --no-root
EXPOSE 8000

COPY . .

CMD ["uvicorn", "src.main:app", "--reload"]
