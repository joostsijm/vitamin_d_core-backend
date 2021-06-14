.PHONY: FORCE up down logs

main: build

build:
	docker-compose build

up: up-dev

up-dev:
	docker-compose --env-file .env.dev up -d

up-prod:
	docker-compose --env-file .env.prod up -d

down:
	docker-compose down

logs:
	docker-compose logs -tf

restart: down build up
