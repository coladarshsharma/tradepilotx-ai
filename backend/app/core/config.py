from functools import lru_cache
from typing import Literal

from pydantic import AnyUrl, EmailStr, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application configuration loaded from environment variables."""

    app_name: str = "TradePilotX AI"
    environment: Literal["development", "test", "production"] = "development"
    debug: bool = False
    api_v1_prefix: str = "/api/v1"
    database_url: str = "postgresql+psycopg2://tradepilotx:tradepilotx@db:5432/tradepilotx"
    secret_key: str = Field(min_length=32)
    algorithm: str = "HS256"
    access_token_expire_minutes: int = Field(default=30, gt=0)
    refresh_token_expire_days: int = Field(default=14, gt=0)
    password_reset_expire_minutes: int = Field(default=30, gt=0)
    email_verification_expire_hours: int = Field(default=24, gt=0)
    cors_origins: list[AnyUrl] = []

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
