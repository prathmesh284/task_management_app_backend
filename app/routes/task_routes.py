from fastapi import APIRouter, Depends
from app.database import get_db
from app.dependencies import get_current_user
from app.schemas.task import TaskCreateSchema
from app.controllers import task_controller

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/")
def create(task: TaskCreateSchema, db=Depends(get_db), user=Depends(get_current_user)):
    return task_controller.create_task(db, task, user)

@router.get("/my")
def my_tasks(db=Depends(get_db), user=Depends(get_current_user)):
    return task_controller.my_tasks(db, user)
