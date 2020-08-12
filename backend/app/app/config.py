from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    DATABASE_SERVER: str
    DATABASE_DB: str
    DATABASE_URL: str = f"postgres://{POSTGRES_USER}:t3st3123@db/easy_money"
    DATABASE_TIMEOUT: int

    class Config:
        env_file = ".env"


settings = Settings()
