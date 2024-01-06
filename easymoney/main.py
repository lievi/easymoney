import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from easymoney.api.routes import api_router
from easymoney.config import settings
from easymoney.db.sqlmodel import create_db_and_tables

# TODO: get the config from the yaml file
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)
swagger_config = {"syntaxHighlight.theme": "obsidian"}


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(
    title="Easy Money", swagger_ui_parameters=swagger_config, lifespan=lifespan
)

app.include_router(api_router, prefix=settings.API_V1_STR)


logger.info("Starting the app")
