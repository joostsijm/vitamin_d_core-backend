# syntax=docker/dockerfile:1

FROM python:3.9-slim

WORKDIR /usr/src/app

COPY . .
RUN pip3 install .

COPY production.env .env

CMD "vitamin_d_resource_user"
