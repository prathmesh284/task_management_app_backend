from fastapi import APIRouter, Depends
from app.database import get_db
from app.dependencies import get_current_user
from app.schemas.task import TaskCreateSchema, TaskResponseSchema, TaskStatusUpdateSchema
from app.controllers import task_controller

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/")
def create(task: TaskCreateSchema, db=Depends(get_db), user=Depends(get_current_user)):
    created_task = task_controller.create_task(db, task, user)
    return TaskResponseSchema(**created_task)

@router.get("/")
def get_all_tasks(db=Depends(get_db)):
    tasks = task_controller.all_tasks(db);
    return [TaskResponseSchema(**t) for t in tasks]

@router.get("/my")
def my_tasks(db=Depends(get_db), user=Depends(get_current_user)):
    tasks = task_controller.my_tasks(db, user)
    return [TaskResponseSchema(**t) for t in tasks]

@router.patch("/{task_id}/status")
def update_status(task_id: int, payload: TaskStatusUpdateSchema, db=Depends(get_db), user=Depends(get_current_user)):
    return task_controller.update_task_status(db, task_id, payload, user)