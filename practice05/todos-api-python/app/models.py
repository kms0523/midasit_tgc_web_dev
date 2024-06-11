from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String(255))
    start_time = Column(Integer)
    end_time = Column(Integer)
    done = Column(Boolean)

class TodoDailyComment(Base):
    __tablename__ = "TodoDailyComment"
    date = Column(Integer, primary_key=True)
    comment = Column(String(255))