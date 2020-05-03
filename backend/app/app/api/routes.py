from fastapi import APIRouter

from app.api.resources import expenses, healthcheck


api_router = APIRouter()
api_router.include_router(healthcheck.router, tags=["healthcheck"])
api_router.include_router(
    expenses.router, prefix="/expenses", tags=["expenses"]
)
