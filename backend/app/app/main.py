# import logging
# import os
# import yaml

from fastapi import FastAPI

from app.infrastructure.api.routes import api_router

# Setting the logs
# with open('app/logconf.yaml', 'r') as f:
#     config = yaml.safe_load(f.read())
#     logging.config.dictConfig(config)

# logger = logging.getLogger(__name__)

app = FastAPI(title="Easy Money")

app.include_router(
    api_router, prefix="/api/v1"
)  # TODO: include this prefix on settings.

# logger.info('Starting the app')
# TODO: Add the shutdown event to disconnect to the database