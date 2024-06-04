FROM python:3.11

RUN apt-get update

WORKDIR /app

ADD . /app
EXPOSE 8888
