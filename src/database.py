from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase
from sqlalchemy import URL, create_engine, text
from config import settings

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
