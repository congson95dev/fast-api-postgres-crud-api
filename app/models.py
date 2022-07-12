from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .config import Base


class Book(Base):
    __tablename__ ="book"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)

    # relation
    r_bookmark = relationship("BookMark", back_populates="r_book")


class BookMark(Base):
    __tablename__ ="bookmark"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    book_id = Column(Integer, ForeignKey("book.id", ondelete='CASCADE'), nullable=False)

    # relation
    r_book = relationship("Book", back_populates="r_bookmark")
