from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    DATABASE_URL: Optional[str] = None
    OPENAI_API_KEY: Optional[str] = None

settings = Settings()
