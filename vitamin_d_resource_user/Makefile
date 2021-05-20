.PHONY: FORCE build start stop rm logs

-include .env
export

name = $(notdir $(CURDIR))

main: build

build:
	docker build -t $(name) .

start:
	docker run --name $(name) -dp 8080:8080 $(name)

stop:
	docker stop $(name)

rm: stop
	docker rm $(name)

logs:
	docker logs $(name)

restart: stop rm build start logs
