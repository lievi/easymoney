import logging
from fastapi import APIRouter

router = APIRouter()


@router.get("/ping")
async def ping() -> str:
    """Heathcheck endpoint"""
    return "pong"
