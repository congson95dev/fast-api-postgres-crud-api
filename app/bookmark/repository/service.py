from sqlalchemy.orm import Session
from ...models import Book, BookMark
from ..schemas.bookmark import BookMarkBase
from fastapi import HTTPException


def get_bookmarks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(BookMark).offset(skip).limit(limit).all()


def get_bookmark(db: Session, bookmark_id: int):
    return db.query(BookMark).filter(BookMark.id == bookmark_id).first()


def create_bookmark(db: Session, bookmark: BookMarkBase):
    _book = db.query(Book).filter(Book.id == bookmark.book_id).first()
    if not _book:
        raise HTTPException(status_code=404, detail="Book not found")

    _bookmark = BookMark(title=bookmark.title, description=bookmark.description, book_id=bookmark.book_id)
    db.add(_bookmark)
    db.commit()
    db.refresh(_bookmark)
    return _bookmark


def update_bookmark(db: Session, bookmark_id: int, bookmark):
    _bookmark = get_bookmark(db=db, bookmark_id=bookmark_id)
    if not _bookmark:
        raise HTTPException(status_code=404, detail="Bookmark not found")

    _bookmark.title = bookmark.title or _bookmark.title
    _bookmark.description = bookmark.description or _bookmark.description

    db.commit()
    db.refresh(_bookmark)
    return _bookmark


def remove_bookmark(db: Session, bookmark_id: int):
    _bookmark = get_bookmark(db=db, bookmark_id=bookmark_id)
    if not _bookmark:
        raise HTTPException(status_code=404, detail="Bookmark not found")

    db.delete(_bookmark)
    db.commit()

    return True

