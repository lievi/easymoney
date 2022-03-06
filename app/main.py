import logging

from fastapi import FastAPI

from app.api.routes import api_router
from app.config import settings

# TODO: get the config from the yaml file
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

app = FastAPI(title="Easy Money")

app.include_router(
    api_router, prefix=settings.API_V1_STR
)

logger.info('Starting the app')
