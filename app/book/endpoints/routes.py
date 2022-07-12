from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from ..schemas.book import BookBase, BookResponse, BookUpdate
from typing import List

from ..repository import service

from ...main import get_db

book_router = APIRouter()


@book_router.post("/create", response_model=BookResponse)
async def create_book_service(request: BookBase, db: Session = Depends(get_db)):
    return service.create_book(db, book=request)


@book_router.get("/", response_model=List[BookResponse])
async def get_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return service.get_books(db, skip, limit)


@book_router.get("/{book_id:int}", response_model=BookResponse)
async def get_book(book_id: int, db: Session = Depends(get_db)):
    return service.get_book(db, book_id=book_id)


@book_router.put("/update/{book_id:int}", response_model=BookResponse)
async def update_book(book_id: int, request: BookUpdate, db: Session = Depends(get_db)):
    return service.update_book(db, book_id=book_id, book=request)


@book_router.delete("/delete/{book_id:int}")
async def delete_book(book_id: int, db: Session = Depends(get_db)):
    return service.remove_book(db, book_id=book_id)
