#from database.conn import db
from fastapi.responses import JSONResponse
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session, sessionmaker
from models.test import Test
from dataclasses import asdict
from schemas.user import Item
from sqlalchemy import text
import asyncio
from common.log_config import logger
from decorators.database import transaction

class TestServce:
    async def select(db : Session):
        query = text("SELECT * FROM test")
        # example = db.query(test).all()
        result = db.execute(query).fetchone()
        #item = example[0]
        item = {
            "id" : result[0],
            "name": result[1],
            "number": result[2]
        }
        return JSONResponse(content=item)
    
    @transaction
    async def insert(item : Item, db):
        logger.info(f"## INSERT ITEM INFO : {item.id}, {item.name}, {item.number}")
        print(id(logger))
        try:
            new_item = Test(
                ID = item.id,
                NAME = item.name,
                NUMBER = item.number
            )
            db.add(new_item)
            db.commit()
            
            return JSONResponse(content=asdict(new_item), status_code=200, headers={"Custom-Header": "value"})
        except Exception as e:
            logger.error(f"## ITEM ISNERT ERROR : {e},{e.__traceback__}")
            db.rollback()
            return JSONResponse(content=None, status_code=500, headers={"Custom-Header": "value"})
        

    @transaction
    async def update(item : Item, db):
        logger.info(f"## INSERT UPDATE INFO : {item.id}, {item.name}, {item.number}")
        print(id(logger))
        try:
            new_item = Test(
                ID = item.id,
                NAME = item.name,
                NUMBER = item.number
            )  
            db.add(new_item)
            db.commit()
            return JSONResponse(content=asdict(new_item), status_code=200, headers={"Custom-Header": "value"})
        except Exception as e:
            db.rollback()
            logger.error(f"## ITEM UPDATE ERROR : {e},{e.__traceback__}")
            return JSONResponse(content=None, status_code=500, headers={"Custom-Header": "value"})






