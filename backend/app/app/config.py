from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    DATABASE_TIMEOUT: int

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()
