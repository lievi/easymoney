import logging
import os
import yaml

import uvicorn  # debug only
from fastapi import FastAPI

from infrastructure.api.routes import api_router

# Setting the logs
with open('logconf.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

logger = logging.getLogger(__name__)

app = FastAPI(title="Easy Money")

app.include_router(
    api_router, prefix="/api/v1"
)  # TODO: include this prefix on settings.

logger.info('Starting the app')
# Debug Mode
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
