from sqlalchemy import Integer, Column, String

from database.conn import Base


class BookModel(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)