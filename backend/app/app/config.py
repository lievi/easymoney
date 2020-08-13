from typing import Any, Dict, Optional
from pydantic import BaseSettings, PostgresDsn, validator


class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    DATABASE_SERVER: str
    DATABASE_DB: str
    DATABASE_URL: Optional[PostgresDsn] = None
    DATABASE_TIMEOUT: int

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
            path=f"/{values.get('DATABASE_DB') or ''}"
        )

    class Config:
        env_file = ".env"


settings = Settings()
