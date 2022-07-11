from sqlalchemy.orm import Session
from .models import Book
from .schemas import BookBase
from fastapi import HTTPException


def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Book).offset(skip).limit(limit).all()


def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()


def create_book(db: Session, book: BookBase):
    _book = Book(title=book.title, description=book.description)
    db.add(_book)
    db.commit()
    db.refresh(_book)
    return _book


def update_book(db: Session, book_id: int, book):
    _book = get_book(db=db, book_id=book_id)
    if not _book:
        raise HTTPException(status_code=404, detail="Book not found")

    _book.title = book.title or _book.title
    _book.description = book.description or _book.description

    db.commit()
    db.refresh(_book)
    return _book


def remove_book(db: Session, book_id: int):
    _book = get_book(db=db, book_id=book_id)
    if not _book:
        raise HTTPException(status_code=404, detail="Book not found")

    db.delete(_book)
    db.commit()

    return True

