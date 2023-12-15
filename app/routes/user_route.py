from fastapi import APIRouter, Response, Depends
from database.conn import db
from sqlalchemy.orm import Session
from services.user_service import UserService as userSerivce
from common.log_config import logger

class UserRoute:
    router = APIRouter(
        prefix="/user"
    )

    @router.post(path="/login")
    async def user_login(response : Response, db : Session = Depends(db.session)):
        #사용자 중복 check
        logger.info(" ## LOGINT SUCCESS")
        #user_check_res = userSerivce.check_user_validation()
        return "login"
