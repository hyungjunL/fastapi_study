from fastapi import APIRouter

from services.book_service import save_book
from schemas.book import BookInfo



class BookRoute:
    router = APIRouter(
        prefix="/book"
    )

    @router.post("/save")
    def post_books(book : BookInfo):
        return save_book(book)

