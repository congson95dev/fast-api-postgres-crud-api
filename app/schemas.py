from typing import List, Optional, Generic, TypeVar, Union
from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    description: Union[str, None] = None


class BookResponse(BookBase):
    id: int

    # use this orm_mode = True so it can return the data even if it is not a dict, but an ORM model
    class Config:
        orm_mode = True


class BookUpdate(BaseModel):
    title: Union[str, None] = None
    description: Union[str, None] = None
