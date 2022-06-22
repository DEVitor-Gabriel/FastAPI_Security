from typing import List
import os

from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = f'postgresql+asyncpg://{os.environ["DB_USER"]}:{os.environ["DB_PASSWORD"]}@{os.environ["DB_SERVER"]}:5432/{os.environ["DB_NAME"]}'
    DBBaseModel = declarative_base()

    JWT_SECRET: str = os.environ["JWT_SECRET"]
    """
    import secrets

    token: str = secrets.token_urlsafe(32)
    """
    ALGORITHM: str = 'HS256'
    # 60 minutos * 24 horas * 7 dias => 1 semana
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        case_sensitive = True


settings: Settings = Settings()
