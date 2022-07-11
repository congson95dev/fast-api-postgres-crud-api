from sqlalchemy import Column, Integer, String
from .config import Base


class Book(Base):
    __tablename__ ="book"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
