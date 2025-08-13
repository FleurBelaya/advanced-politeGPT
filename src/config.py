from pydantic_settings import BaseSettings, SettingsConfigDict
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    api_v1_prefix: str = "/api/v1"
    db_echo: bool = False

    SECRET_KEY: str
    MODEL: str
    DEBUG: bool = False

    @property
    def db_url(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file=os.path.join(BASE_DIR, ".env"))

settings = Settings()
