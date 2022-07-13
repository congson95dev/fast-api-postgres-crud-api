from typing import List, Optional, Generic, TypeVar, Union
from pydantic import BaseModel
from ...book.schemas.book import BookResponse


class BookMarkBase(BaseModel):
    page: int
    book_id: int


class BookMarkResponse(BookMarkBase):
    id: int
    # really cool feature here:
    # when we have relation in model, we can use it as a variable here,
    # so it will automatic return the response to us
    # Ex: "r_book" is a relation variable in this "bookmark" table,
    # so we can set it like this:
    r_book: BookResponse

    # use this orm_mode = True so it can return the data even if it is not a dict, but an ORM model
    class Config:
        orm_mode = True


class BookMarkUpdate(BaseModel):
    page: Union[int, None] = None
    book_id: Union[int, None] = None
