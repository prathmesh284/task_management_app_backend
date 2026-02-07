from fastapi import APIRouter, Depends, Query
from app.database import get_db
from app.dependencies import get_current_user
from app.schemas.task import TaskCreateSchema, TaskResponseSchema, TaskStatusUpdateSchema, TaskUpdateSchema
from app.controllers import task_controller

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/", response_model=TaskResponseSchema)
def create(task: TaskCreateSchema, db=Depends(get_db), user=Depends(get_current_user)):
    return task_controller.create_task(db, task, user)

# api for test
@router.get("/all")
def get_all_tasks(db=Depends(get_db)):
    tasks = task_controller.all_tasks(db)
    return [TaskResponseSchema(**t) for t in tasks]

@router.get("/my")
def my_tasks(db=Depends(get_db), user=Depends(get_current_user)):
    tasks = task_controller.my_tasks(db, user)
    return [TaskResponseSchema(**t) for t in tasks]

@router.patch("/{task_id}/status")
def update_status(task_id: int, payload: TaskStatusUpdateSchema, db=Depends(get_db), user=Depends(get_current_user)):
    return task_controller.update_task_status(db, task_id, payload, user)

@router.get("/")
def get_tasks(
    status: str = Query("all", pattern="^(all|Pending|In Progress|Completed)$"),
    page: int = Query(1, ge=1),
    limit: int = Query(9, ge=1, le=50),
    db=Depends(get_db),
    user=Depends(get_current_user)
):
    return task_controller.get_tasks_paginated(
        db=db,
        status=status,
        page=page,
        limit=limit,
        current_user=user
    )

@router.get("/upcoming")
def get_upcoming_tasks(
    days: int = Query(7, ge=1, le=30),
    db=Depends(get_db),
    user=Depends(get_current_user)
):
    return task_controller.get_upcoming_tasks(db, days, user)

@router.get("/count")
def get_count(db=Depends(get_db)):
    return task_controller.get_count_of_all_tasks(db)

@router.put("/{task_id}")
def update_task(
    task_id: int,
    task: TaskUpdateSchema,
    db=Depends(get_db),
    user=Depends(get_current_user),
):
    return task_controller.update_task(db, task_id, task, user)

@router.delete("/{task_id}")
def delete_task(
    task_id: int,
    db=Depends(get_db),
    user=Depends(get_current_user),
):
    return task_controller.delete_task(db, task_id, user)