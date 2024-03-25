from sqlalchemy import ForeignKey, String, Integer
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

class Base(DeclarativeBase):
    pass

class Item(Base):
    __tablename__ = 'items'

    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    code: Mapped[int] = mapped_column(Integer(), unique=True)
    stock: Mapped[int] = mapped_column(Integer(), default=0)
