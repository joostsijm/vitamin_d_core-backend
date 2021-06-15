.PHONY: FORCE build start stop rm logs restart

name = $(notdir $(CURDIR))

main: build

build:
	docker build -t $(name) .

start:
	docker run --name $(name) -dp 5000:5000 $(name)

stop:
	docker stop $(name)

rm: stop
	docker rm $(name)

logs:
	docker logs $(name)

restart: stop rm build start logs
