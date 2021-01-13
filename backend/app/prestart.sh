#! /usr/bin/env bash

# Let the DB start
# TODO: Create an script to verify the inialization of the db
sleep 5;
# Run migrations
alembic upgrade head