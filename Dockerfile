FROM python:3.11

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY . .

# Install poetry and project dependencies
RUN pip3 install poetry
RUN poetry install
RUN poetry run python chiisai/manage.py collectstatic

WORKDIR /usr/src/app/chiisai
