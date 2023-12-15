from typing import List, Optional

from pydantic import BaseModel # 객체 타입설정

#DTO, VO느낌?

class Item(BaseModel):
    id : int = 1
    name : str = "홍길동"
    number : int = 1
    
    class Config:
        orm_mode = True

#로그인 JWT토큰 관련 스키마
class Token(BaseModel):
    access_token : str
    token_type : str