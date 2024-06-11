from pydantic import BaseModel

class TodoBase(BaseModel):
    id: int
    content: str
    done: bool

class TodoCreate(BaseModel):
    content: str
    start_time: int
    end_time: int
    done : bool

class TodoUpdate(BaseModel):
    id: int
    content: str
    done : bool

class Todo(TodoBase):
    id: int

    class Config:
        orm_mode = True


class DailyCommentCreate(BaseModel):
    date:    int
    comment: str