FROM python:3.9-slim

RUN pip install poetry

WORKDIR /compiler

COPY . .

RUN poetry install

WORKDIR src

CMD ["poetry", "run", "python", "main.py"]