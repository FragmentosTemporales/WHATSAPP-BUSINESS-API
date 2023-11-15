FROM python:3.9-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN apt-get update
RUN apt-get install -y gcc libmariadb-dev-compat libmariadb-dev build-essential libpq-dev --no-install-recommends
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

RUN mkdir /scripts
WORKDIR /scripts
COPY . /scripts