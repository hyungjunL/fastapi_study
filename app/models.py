from sqlalchemy import Column, TEXT, INT, BIGINT
from sqlalchemy.ext.declarative import declarative_base
from dataclasses import dataclass

Base = declarative_base()

#DB 각 TABLE 정의

@dataclass
class test(Base):
    __tablename__ = "test"

    ID = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
    NAME = Column(TEXT, nullable=False)
    NUMBER = Column(INT, nullable=False)