from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "KRAMIA"
    app_version: str = "0.1.0"
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 480
    database_url: str
    environment: str = "development"
    debug: bool = True

    class Config:
        env_file = ".env"

settings = Settings()