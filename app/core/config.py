# Store
# Databse URL
# JWT secret
# encryption key
# this loads the settings from the .env file and makes them available as attributes of the settings object
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    database_url: str
    jwt_secret_key: str
    encryption_key: str | None = None

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )

settings = Settings()