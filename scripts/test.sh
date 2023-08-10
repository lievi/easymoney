#! /usr/bin/env sh

# set -e - This command exits the script if any error occurs
set -x

# TODO: remove the dependecies, only start the web
INSTALL_DEV=true \
docker-compose \
-f docker-compose.yml -f docker-compose.test.yml \
config > docker-stack.yml

docker-compose -f docker-stack.yml down -v --remove-orphans # Remove possibly previous broken stacks left hanging after an error
docker-compose -f docker-stack.yml up -d
docker-compose -f docker-stack.yml exec -T web pytest --cov
docker-compose -f docker-stack.yml down -v --remove-orphans
rm docker-stack.yml
