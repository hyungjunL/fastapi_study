# from dataclasses import asdict
# import uvicorn
# from fastapi import FastAPI
# from fastapi.middleware import Middleware
# from fastapi.middleware.cors import CORSMiddleware
# # from routes.user_route import UserRoute as userRoute
# from routes import user_route
# from database.conn import db
# from common.config import conf
# from common.log_config import logger
# from routes.test_route import TestRoute as testRoute
# from middlewares.some_middelware import LoggingMiddleware
# # from task.test_task import TestTask, SecondTask
# from extensions.database import Base, engine

# Base.metadata.create_all(bind=engine)

# middleware = [
#     Middleware(LoggingMiddleware)
# ]

# def create_app():
#     app = FastAPI(middleware=middleware)
#     # config 설정들 가져오기
#     c = conf()
#     conf_dict = asdict(c)
#     # 데이터 베이스 이니셜라이즈
#     db.init_app(app, **conf_dict)
    
#     # 라우터 정의
#     app.include_router(testRoute.router, tags=["TEST"])
#     app.include_router(user_route.router, tags=["USER"])
    
#     return app


# app = create_app()

# if __name__ == "__main__":
#     logger.info("APPLICATION STARTED")
#     # 스케쥴러 시작 You should start your Thread before calling uvicorn.run, as uvicorn.run is blocking the thread.
#     #TestTask.sched.start()
#     #SecondTask.sched.start()
#     uvicorn.run("main:app", host="192.168.1.153", port=8080, reload=True, workers=4)


import uvicorn
from fastapi import FastAPI
from fastapi.middleware import Middleware
from database.conn import Base, engine
from middlewares.some_middelware import LoggingMiddleware
from routes.test_route import TestRoute as test_route
from routes.user_route import UserRoute as user_route
from routes.book_route import BookRoute as book_route

Base.metadata.create_all(bind=engine)

middleware = [
    Middleware(LoggingMiddleware)
]

def create_app():
    app = FastAPI(middleware=middleware)
    
    # 라우터 정의
    app.include_router(book_route.router, tags=["BOOK"])
    app.include_router(test_route.router, tags=["TEST"])
    app.include_router(user_route.router, tags=["USER"])
    
    return app


app = create_app()

if __name__ == '__main__':
    uvicorn.run("main:app", host="192.168.1.153", port=8080, reload=True)