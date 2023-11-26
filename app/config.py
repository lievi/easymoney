from pydantic import BaseSettings


class Settings(BaseSettings):
    # API Config
    API_V1_STR: str = "/api/v1"

    DATABASE_TIMEOUT: int
    DATABASE_URL: str

    # model_config = ConfigDict(env_file=".env")
    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'


settings = Settings()
