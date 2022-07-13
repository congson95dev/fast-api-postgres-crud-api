from typing import List, Optional, Generic, TypeVar, Union
from pydantic import BaseModel
from ...book.schemas.book import BookResponse
from ...bookmark.schemas.bookmark import BookMarkResponse


class BookNoteBase(BaseModel):
    page: int
    line: int
    note: str
    book_id: int

    # use this orm_mode = True so it can return the data even if it is not a dict, but an ORM model
    class Config:
        orm_mode = True


class BookNoteResponse(BookNoteBase):
    id: int


class BookNoteJoinDataResponse(BaseModel):
    booknote: BookNoteResponse
    r_book: BookResponse
    r_bookmark: BookMarkResponse

    # use this orm_mode = True so it can return the data even if it is not a dict, but an ORM model
    class Config:
        orm_mode = True
