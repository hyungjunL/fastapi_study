from database.conn import db
from fastapi.responses import JSONResponse
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session, sessionmaker
from models import test
from dataclasses import asdict
from database.schemas import item
from sqlalchemy import text
import asyncio
from common.log_config import logger

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

async def insert(item : item, db : Session):
    
    logger.info(f"## INSERT ITEM INFO : {item.id}, {item.name}, {item.number}")
    print(id(logger))
    try:
        new_item = test(
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
    


async def update(item : item,db : Session):

    logger.info(f"## INSERT UPDATE INFO : {item.id}, {item.name}, {item.number}")
    print(id(logger))
    try:
        new_item = test(
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











