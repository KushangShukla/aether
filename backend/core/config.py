from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
    """
    Centralized configuration for AETHER.
    Values are loaded from .env automatically.
    """

    APP_NAME:str="AETHER"
    APP_VERSION:str="0.1.0"

    OLLAMA_URL:str="http://localhost:11434/api/generate"
    DEFAULT_MODEL:str="qwen3:8b"

    DEBUG:bool=True

    DATABASE_USER:str="postgres"
    DATABASE_PASSWORD:str=""
    DATABASE_HOST:str="localhost"
    DATABASE_PORT:int=5432
    DATABASE_NAME:str="aether"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8",extra="ignore")

settings = Settings()
