# Define required macros here
SHELL = /bin/sh

up:
	docker-compose -f docker-compose.yml -f docker-compose.test.yml up -d

test:
	$(SHELL) scripts/test.sh

start-dependencies-locally:
	docker-compose -f docker-compose.yml -f docker-compose.devel.yml up -d db

down:
	docker-compose down -v
