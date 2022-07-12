from fastapi import FastAPI
from . import models
from .config import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


from .book.endpoints.routes import book_router
from .bookmark.endpoints.routes import bookmark_router
from .config import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(book_router, prefix="/book", tags=["book"])
app.include_router(bookmark_router, prefix="/bookmark", tags=["bookmark"])


