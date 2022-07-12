from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from ..schemas.bookmark import BookMarkBase, BookMarkResponse, BookMarkUpdate
from typing import List

from ..repository import service

from ...main import get_db

bookmark_router = APIRouter()


@bookmark_router.post("/create", response_model=BookMarkResponse)
async def create_bookmark_service(request: BookMarkBase, db: Session = Depends(get_db)):
    return service.create_bookmark(db, bookmark=request)


@bookmark_router.get("/", response_model=List[BookMarkResponse])
async def get_bookmarks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return service.get_bookmarks(db, skip, limit)


@bookmark_router.get("/{bookmark_id:int}", response_model=BookMarkResponse)
async def get_bookmark(bookmark_id: int, db: Session = Depends(get_db)):
    return service.get_bookmark(db, bookmark_id=bookmark_id)


@bookmark_router.put("/update/{bookmark_id:int}", response_model=BookMarkResponse)
async def update_bookmark(bookmark_id: int, request: BookMarkUpdate, db: Session = Depends(get_db)):
    return service.update_bookmark(db, bookmark_id=bookmark_id, bookmark=request)


@bookmark_router.delete("/delete/{bookmark_id:int}")
async def delete_bookmark(bookmark_id: int, db: Session = Depends(get_db)):
    return service.remove_bookmark(db, bookmark_id=bookmark_id)
