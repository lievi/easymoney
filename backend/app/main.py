import uvicorn  # debug only
from fastapi import FastAPI

from api.v1 import api

app = FastAPI(title="Easy Money")

app.include_router(
    api.api_router, prefix="/api/v1"
)  # TODO: include this prefix on settings


# Debug Mode
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
