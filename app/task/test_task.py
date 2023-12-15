from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler
from common.log_config import logger
import asyncio

async def real_job():           
        while True:
            logger.info("#### INTERVAL ....")
            await asyncio.sleep(1.0)

class TestTask:
    sched = BackgroundScheduler(timezone='Asia/Seoul')

    @sched.scheduled_job('interval', seconds=10, id='test')
    def job():
        asyncio.run(real_job())
    
    

class SecondTask:
    sched = BackgroundScheduler(timezone='Asia/Seoul')

    @sched.scheduled_job('interval', seconds=10, id='test2')
    def job():
        logger.info("#### SecondTask INTERVAL ....")
