.PHONY: FORCE up

main: build

build:
	docker-compose build

up:
	docker-compose up
