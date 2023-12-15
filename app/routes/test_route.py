from fastapi import APIRouter, Depends
from services.test_service import TestService as testService
from sqlalchemy.orm import Session
from database.conn import db
from database.schemas import Item

class TestRoute:

    router = APIRouter(
        prefix="/test"
    )

    @router.get("/select")#,response_model=Item)
    async def test(db : Session = Depends(db.session)):
        return testService.select(db=db)

    @router.post("/insert")#,response_model=Item)
    async def test(item : Item,db : Session = Depends(db.session)):
        return await testService.insert(item, db=db)

    @router.post("/update")#,response_model=Item)
    async def test(item : Item, db : Session = Depends(db.session)):
        return await testService.update(item, db=db)