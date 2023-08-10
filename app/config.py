from pydantic_settings import SettingsConfigDict, BaseSettings


class Settings(BaseSettings):
    # API Config
    API_V1_STR: str = "/api/v1"

    DATABASE_TIMEOUT: int
    DATABASE_URL: str 
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
