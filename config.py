# config.py
from pydantic import BaseSettings


class Settings(BaseSettings):
    MONGODB_CONNECTION: str

    class Config:
        env_file = ".env"
