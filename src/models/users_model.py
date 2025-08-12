import datetime
from typing import Optional, Annotated
from sqlalchemy import TIMESTAMP, Enum, Table, Column, Integer, String, MetaData, ForeignKey, func, text
from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base
import enum

class WorkersOrm(Base):
    __table_args__ = {"schema": "public"}
    __tablename__ = 'workers'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]