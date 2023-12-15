from sqlalchemy.orm import Session
from sqlalchemy import text
from fastapi.responses import JSONResponse

class UserService:
    async def check_user_validation(db : Session):
        query = text("SELECT COUNT(*) FROM test")
        # example = db.query(test).all()
        result = db.execute(query).fetchone()
        #item = example[0]
        item = {
            "id" : result[0],
            "name": result[1],
            "number": result[2]
        }
        return JSONResponse(content=item)