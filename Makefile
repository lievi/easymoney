# Define required macros here
SHELL = /bin/sh

run-docker-dev:
	docker run -p 80:80 -v $(pwd):/app easymoney:latest /start-reload.sh