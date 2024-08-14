#
FROM python:3.9

#
WORKDIR /code

#
RUN pip install poetry

#
COPY ./pyproject.toml ./poetry.lock* /code/

#
RUN poetry install

#
COPY ./app /code/app

#
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
