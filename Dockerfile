FROM python:3.8.6-slim

RUN apt-get update
RUN apt-get install -y gettext

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

WORKDIR /code

COPY . /code/
