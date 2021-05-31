.PHONY: FORCE up down logs

main: build

build:
	docker-compose build

up:
	docker-compose up -d
	docker-compose logs -t

down:
	docker-compose down

logs:
	docker-compose logs -tf
