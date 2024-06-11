from sqlalchemy.orm import Session
from app.models import Todo
from app.schema import DailyCommentCreate
from app.schema import TodoUpdate

from app.models import TodoDailyComment


# todo
def get_todos(db: Session):
    return db.query(Todo).all()

def get_todo(db: Session, todo_id: int):
    return db.query(Todo).filter(Todo.id == todo_id).first()

def create_todo(db: Session, todo: DailyCommentCreate):
    db_todo = Todo(**todo.dict())

    if not 0 <= db_todo.start_time <= 24:
        return False

    if not 0 <= db_todo.end_time <= 24:
        return False

    if db_todo.start_time > db_todo.end_time:
        return False
    
    db.add(db_todo)
    db.commit()

    return True

def update_todo(db: Session, todo: Todo, updated_todo: TodoUpdate):
    for key, value in updated_todo.dict().items():
        setattr(todo, key, value)
    db.commit()

def delete_todo(db: Session, todo: Todo):
    db.delete(todo)
    db.commit()


#daily commnet
def get_all_daily_comment(db: Session):
    return db.query(TodoDailyComment).all()   

def get_daily_comment(db: Session, date: int):
    return db.query(TodoDailyComment).filter(TodoDailyComment.date == date).first()

def create_daily_comment(db: Session, daily_comment: DailyCommentCreate):
    db_daily_comment = TodoDailyComment(**daily_comment.dict())
    db.add(db_daily_comment)
    db.commit()

