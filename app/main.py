from dataclasses import asdict
import uvicorn
from fastapi import FastAPI
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from database.conn import db
from common.config import conf
from common.log_config import logger
from routes import test_route
from middlewares.some_middelware import LoggingMiddleware,CorsMiddleware
from task.test_task import TestTask, SecondTask

middleware = [
    Middleware(LoggingMiddleware),
    CORSMiddleware(CorsMiddleware)
]

def create_app():
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.add_middleware(
        Middleware
    )
    # config 설정들 가져오기
    c = conf()
    conf_dict = asdict(c)
    # 데이터 베이스 이니셜라이즈
    db.init_app(app, **conf_dict)
    
    # 라우터 정의
    app.include_router(test_route.router, tags=["TEST"])
    
    return app


app = create_app()

if __name__ == "__main__":
    logger.info("APPLICATION STARTED")
    # 스케쥴러 시작 You should start your Thread before calling uvicorn.run, as uvicorn.run is blocking the thread.
    #TestTask.sched.start()
    #SecondTask.sched.start()
    uvicorn.run("main:app", host="192.168.1.153", port=8080, reload=True)