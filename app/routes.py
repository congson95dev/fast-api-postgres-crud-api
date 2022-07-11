from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from .config import SessionLocal
from sqlalchemy.orm import Session
from .schemas import BookBase, BookResponse, BookUpdate
from typing import List

from . import crud

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/create", response_model=BookResponse)
async def create_book_service(request: BookBase, db: Session = Depends(get_db)):
    return crud.create_book(db, book=request)


@router.get("/", response_model=List[BookResponse])
async def get_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_books(db, skip, limit)


@router.get("/{book_id:int}")
async def get_book(book_id: int, db: Session = Depends(get_db)):
    return crud.get_book(db, book_id=book_id)


@router.put("/update/{book_id:int}")
async def update_book(book_id: int, request: BookUpdate, db: Session = Depends(get_db)):
    return crud.update_book(db, book_id=book_id, book=request)


@router.delete("/delete/{book_id:int}")
async def delete_book(book_id: int, db: Session = Depends(get_db)):
    return crud.remove_book(db, book_id=book_id)
