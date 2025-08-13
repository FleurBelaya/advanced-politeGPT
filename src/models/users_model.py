from sqlalchemy import Column, String
from sqlalchemy.orm import Mapped, mapped_column
from pydantic import EmailStr

from .base import Base

class UsersOrm(Base):
    __tablename__ = "Users"
    __table_args__ = {"schema": "public"}

    # Колонки базы данных
    username: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)

