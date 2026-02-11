
from fastapi import FastAPI, Depends, HTTPException
from typing import List
from .models import Task, TaskCreate
from .repositories import InMemoryTaskRepository, ITaskRepository, SqlTaskRepository
from .services import TaskService
from .database import SessionLocal, engine
from sqlalchemy.orm import Session
from . import models_orm
from app.database import engine
from app.models_orm import Base

Base.metadata.create_all(bind=engine)

models_orm.Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_task_service(db: Session = Depends(get_db)):
    repo = SqlTaskRepository(db)
    return TaskService(repo)

@app.get("/tasks", response_model=List[Task])
def read_tasks(service: TaskService = Depends(get_task_service)):
    return service.get_tasks()

@app.post("/tasks", response_model=Task)
def create_task(task: TaskCreate, service: TaskService = Depends(get_task_service)):
    # เรียก Service ซึ่งภายในมีการเช็ค Exception ไว้แล้ว
    # ถ้าชื่อซ้ำ API จะ return 400 Bad Request ให้เอง
    return service.create_task(task)

@app.put("/tasks/{task_id}/complete", response_model=Task)
def complete_task(task_id: int, service: TaskService = Depends(get_task_service)):
    updated_task = service.mark_as_complete(task_id)
    if updated_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
   