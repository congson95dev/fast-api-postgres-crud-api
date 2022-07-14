from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from ..schemas.booknote import BookNoteBase, BookNoteResponse, BookNoteJoinDataResponse
from typing import List

from ..repository import service

from ...main import get_db

booknote_router = APIRouter()


@booknote_router.post("/create", response_model=BookNoteBase)
async def create_booknote_service(request: BookNoteBase, db: Session = Depends(get_db)):
    return service.create_booknote(db, book=request)


@booknote_router.get("/", response_model=List[BookNoteResponse])
async def get_booknotes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return service.get_booknotes(db, skip, limit)


@booknote_router.get("/join-data", response_model=List[BookNoteJoinDataResponse])
async def get_booknotes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return service.get_booknotes_join_data(db, skip, limit)
