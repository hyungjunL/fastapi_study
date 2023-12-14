from fastapi import APIRouter, Depends
from services import test_service
from sqlalchemy.orm import Session
from database.conn import db
from database.schemas import item

router = APIRouter(
    prefix="/radar"
)

@router.get("/select")#,response_model=item)
async def test(db : Session = Depends(db.session)):
    return test_service.select(db=db)

@router.post("/insert")#,response_model=item)
async def test(item : item,db : Session = Depends(db.session)):
    return await test_service.insert(item, db=db)

@router.post("/update")#,response_model=item)
async def test(item : item, db : Session = Depends(db.session)):
    return await test_service.update(item, db=db)