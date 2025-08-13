from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import create_engine
from src.config import settings

print(settings.DB_NAME)
print(settings.DATABASE_URL_psycopg)
engine = create_engine(
    url = settings.DATABASE_URL_psycopg,
    echo=True,
    pool_size=5,
    max_overflow=10
)

session_factory = sessionmaker(engine)

class Base(DeclarativeBase):
    pass
