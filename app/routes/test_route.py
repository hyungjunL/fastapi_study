from fastapi import APIRouter, Depends
from services.test_service import TestServce as testService
from sqlalchemy.orm import Session
from schemas.user import Item

class TestRoute:

    router = APIRouter(
        prefix="/test"
    )

    @router.get("/select")#,response_model=Item)
    async def test():
        return testService.select()

    # @router.post("/insert")#,response_model=Item)
    # async def test(item : Item,db : Session = Depends(db.session)):
    #     return await testService.insert(item, db=db)

    @router.post("/insert")#,response_model=Item)
    async def test(item : Item):
        return await testService.insert(item)

    @router.post("/update")#,response_model=Item)
    async def test(item : Item):
        return await testService.update(item)
    
    @router.post("/test/insert")#,response_model=Item)
    async def test(item : Item):
        return await testService.test_insert(item)

