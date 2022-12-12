from pydantic import BaseSettings
from app import BASE_DIR


class Settings(BaseSettings):
    DATABASE_STRING: str
    API_KEY: str

    class Config:
        env_file = BASE_DIR.joinpath('.env')
        env_file_encoding = 'utf-8'


settings = Settings()
