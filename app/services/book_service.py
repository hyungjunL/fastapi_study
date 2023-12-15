from decorators.database import transaction
from models.book import BookModel
from schemas.book import BookInfo
from fastapi.responses import JSONResponse
from common.log_config import logger

@transaction
def save_book(book,db):
    try:
        logger.info(f"## INSERT ITEM INFO : {book.title}, {book.id}")
        db.add(BookModel(title=book.title,id=book.id))
        return JSONResponse(content=None, status_code=200, headers={"Custom-Header": "value"})
    except:
        return JSONResponse(content=None, status_code=400, headers={"Custom-Header": "value"})
