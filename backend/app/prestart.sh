#! /usr/bin/env bash

# Let the DB start
python app/verify_dependencies.py

# Run migrations
alembic upgrade head