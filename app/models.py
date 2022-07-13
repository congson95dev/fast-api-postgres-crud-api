from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .config import Base


class Book(Base):
    __tablename__ ="book"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)

    # relation
    # to make the relation/foreignkey work, you need to add relationship in both table, parent and child
    # for cascade, you need to add cascade in parent table, not child table.
    # https://stackoverflow.com/questions/72950729/fastapi-postgres-cascade-delete
    r_bookmark = relationship("BookMark", back_populates="r_book", cascade="all,delete")
    r_booknote = relationship("BookNote", back_populates="r_book", cascade="all,delete")


class BookMark(Base):
    __tablename__ ="bookmark"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    page = Column(Integer, nullable=False)
    book_id = Column(Integer, ForeignKey("book.id"), nullable=False)

    # relation
    # to make the relation/foreignkey work, you need to add relationship in both table, parent and child
    r_book = relationship("Book", back_populates="r_bookmark")


class BookNote(Base):
    __tablename__ ="booknote"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    page = Column(Integer, nullable=False)
    line = Column(Integer, nullable=False)
    note = Column(String, nullable=False)
    book_id = Column(Integer, ForeignKey("book.id"), nullable=False)

    # relation
    # to make the relation/foreignkey work, you need to add relationship in both table, parent and child
    r_book = relationship("Book", back_populates="r_booknote")
