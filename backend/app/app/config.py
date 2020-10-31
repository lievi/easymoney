from typing import Any, Dict, Optional
from pydantic import BaseSettings, PostgresDsn, validator


class Settings(BaseSettings):
    DATABASE_URL: Optional[PostgresDsn] = None
    POSTGRES_USER: str = None
    POSTGRES_PASSWORD: str = None
    POSTGRES_DB: str = None
    DATABASE_SERVER: str = None
    DATABASE_TIMEOUT: int = None

    @validator("DATABASE_URL", pre=True)
    def create_postgres_connection_dns(
        cls, v: Optional[str], values: Dict[str, Any]
    ) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get('POSTGRES_USER'),
            password=values.get('POSTGRES_PASSWORD'),
            host=values.get('DATABASE_SERVER'),
            path=f"/{values.get('POSTGRES_DB') or ''}"
        )

    class Config:
        env_file = ".env"


settings = Settings()
