from fastapi import HTTPException
from .repositories import ITaskRepository
from .models import TaskCreate

class TaskService:
    def __init__(self, repo: ITaskRepository):
        self.repo = repo

    def get_tasks(self):
        return self.repo.get_all()

    def create_task(self, task_in: TaskCreate):
        # Validation Logic: ห้ามชื่อซ้ำ
        existing_task = self.repo.get_by_title(task_in.title)
        if existing_task:
            raise HTTPException(
                status_code=400, 
                detail=f"Task with title '{task_in.title}' already exists."
            )
        
        # ถ้าไม่ซ้ำ ก็สร้างตามปกติ
        return self.repo.create(task_in)
    
    def mark_as_complete(self, task_id: int):
        return self.repo.update_status(task_id, completed=True)