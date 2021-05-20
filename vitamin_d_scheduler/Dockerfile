# syntax=docker/dockerfile:1

FROM python:3.9-slim

WORKDIR /app

# COPY setup.py setup.py
# COPY README.md README.md 
COPY . .
RUN pip3 install .

COPY production.env .env

# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
CMD "vitamin_d_scheduler"
