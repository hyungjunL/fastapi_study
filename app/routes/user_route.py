from fastapi import APIRouter, Response, Depends, Request
from sqlalchemy.orm import Session
from services.user_service import UserService as userSerivce
from common.log_config import logger
import asyncio
import requests
import os
import threading
from decorators.database import transaction

class UserRoute:
    router = APIRouter(
        prefix="/user"
    )

    @transaction
    @router.get(path="/login")
    async def user_login(response : Response, db):
        #사용자 중복 check
        logger.info(" ## LOGINT SUCCESS")
        
        
        print("## 1 - pid ",os.getpid())
        print("## 1 - thread ",threading.current_thread())
        print("## 1 - native ",threading.get_native_id())
        await asyncio.sleep(15.0)
        await test()
        # await asyncio.sleep(30.0)
        #user_check_res = userSerivce.check_user_validation()
        return "login"

async def test():
    #사용자 중복
    await asyncio.sleep(15.0)
    print("## 2", os.getpid())
    print("## 2 - thread ",threading.current_thread())
    print("## 2 - native ",threading.get_native_id())


    
        
