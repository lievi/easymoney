# Define required macros here
SHELL = /bin/sh

up:
	docker-compose up -d --build

test:
	$(SHELL) scripts/test.sh

start-dependencies-locally:
	docker-compose up -d db

down:
	docker-compose down -v