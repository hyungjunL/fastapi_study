from fastapi import Response, Request
from starlette.background import BackgroundTask
from starlette.types import Message
import logging
from common.log_config import logger

class LoggingMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        logger.info("============================================")
        logger.info("==                                        ==")
        logger.info(f"==        Request URI : {scope["path"]}      ==")
        logger.info("==                                        ==")
        logger.info("============================================")
        print("Request received:",receive)
        await self.app(scope, receive, send)
        logger.info("============================================")
        logger.info("==                                        ==")
        logger.info("==                Response                ==")
        logger.info("==                                        ==")
        logger.info("============================================")
        print("Response sent",send)


    