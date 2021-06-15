# syntax=docker/dockerfile:1

FROM python:3.9-slim

WORKDIR /usr/src/app

COPY src/vitamin_d_resource_user/__main__.py src/vitamin_d_resource_user/__main__.py
COPY README.md README.md
COPY setup.py setup.py
RUN pip3 install -e .

COPY . .

CMD "vitamin_d_resource_user"
