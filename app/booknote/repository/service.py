from sqlalchemy.orm import Session
from ...models import Book, BookMark, BookNote
from ..schemas.booknote import BookNoteBase


def get_booknotes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(BookNote).offset(skip).limit(limit).all()


def get_booknotes_join_data(db: Session, skip: int = 0, limit: int = 100):
    # join table
    # using db.query(table1, table 2)
    # then .filter(), inside we set the table1.id = table2.foreign_key
    result = db.query(Book, BookMark, BookNote).filter(
        Book.id == BookMark.book_id,
    ).filter(
        Book.id == BookNote.book_id,
    ).offset(skip).limit(limit).all()

    response_data = []

    for objects in result:
        response_data.append({
            "book": objects[0],
            "bookmark": objects[1] or None,
            "booknote": objects[2] or None
        })

    return response_data


def create_booknote(db: Session, book: BookNoteBase):
    # we can use **book.dict() like below,
    # so it can transfer full the body instead of transfer each element inside the body
    _booknote = BookNote(**book.dict())
    db.add(_booknote)
    db.commit()
    db.refresh(_booknote)
    return _booknote
