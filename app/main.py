import logging

from fastapi import FastAPI

from app.api.routes import api_router
from app.config import settings
from app.db.sqlmodel import create_db_and_tables

# TODO: get the config from the yaml file
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)
swagger_config = {
    "syntaxHighlight.theme": "obsidian"
}

app = FastAPI(title="Easy Money", swagger_ui_parameters=swagger_config)

app.include_router(api_router, prefix=settings.API_V1_STR)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


logger.info("Starting the app")
