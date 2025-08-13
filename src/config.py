from dataclasses import dataclass
from environs import Env
from pydantic_settings import BaseSettings, SettingsConfigDict
import os


@dataclass
class DatabaseConfig:
    database_url: str


@dataclass
class Config:
    db: DatabaseConfig
    secret_key: str
    debug: bool


def load_config(path: str = None) -> Config:
    env = Env()
    env.read_env(path)

    return Config(
        db=DatabaseConfig(database_url=env("DATABASE_URL")),
        secret_key=env("SECRET_KEY"),
        debug=env.bool("DEBUG", default=False)
    )


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def db_url(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    # @property
    # def DATABASE_URL_psycopg(self):
    #     return f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
