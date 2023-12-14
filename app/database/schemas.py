from typing import List, Optional

from pydantic import BaseModel # 객체 타입설정

#DTO, VO느낌?

class item(BaseModel):
    id : int = 1
    name : str = "홍길동"
    number : int = 1
    
    class Config:
        orm_mode = True