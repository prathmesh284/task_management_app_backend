"""
Task Routes
-----------
This module defines API endpoints related to task management.
Routes handle request validation, authentication, and delegate
business logic to the task controller.
"""

from fastapi import APIRouter, Depends, Query
from app.database import get_db
from app.dependencies import get_current_user
from app.schemas.task import (
    TaskCreateSchema,
    TaskResponseSchema,
    TaskStatusUpdateSchema,
    TaskUpdateSchema
)
from app.controllers import task_controller


# Router configuration
router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.post("/", response_model=TaskResponseSchema)
def create(
    task: TaskCreateSchema,
    db=Depends(get_db),
    user=Depends(get_current_user)
):
    """
    Create a new task.

    Access Control:
        Admin only.

    Request Body:
        TaskCreateSchema

    Returns:
        TaskResponseSchema: Newly created task
    """
    return task_controller.create_task(db, task, user)


# -----------------------------
# Testing / Utility Endpoints
# -----------------------------

@router.get("/all")
def get_all_tasks(db=Depends(get_db)):
    """
    Retrieve all tasks (testing/debug endpoint).

    Returns:
        list[TaskResponseSchema]: List of all tasks
    """
    tasks = task_controller.all_tasks(db)
    return [TaskResponseSchema(**t) for t in tasks]


@router.get("/my")
def my_tasks(
    db=Depends(get_db),
    user=Depends(get_current_user)
):
    """
    Retrieve tasks assigned to the current user.

    Returns:
        list[TaskResponseSchema]: User's tasks
    """
    tasks = task_controller.my_tasks(db, user)
    return [TaskResponseSchema(**t) for t in tasks]


@router.patch("/{task_id}/status")
def update_status(
    task_id: int,
    payload: TaskStatusUpdateSchema,
    db=Depends(get_db),
    user=Depends(get_current_user)
):
    """
    Update the status of a task.

    Rules:
        - Only the assigned user can update the task
        - Status must follow valid workflow transitions

    Request Body:
        TaskStatusUpdateSchema

    Returns:
        dict: Updated task status
    """
    return task_controller.update_task_status(
        db,
        task_id,
        payload,
        user
    )


@router.get("/")
def get_tasks(
    status: str = Query(
        "all",
        pattern="^(all|Pending|In Progress|Completed)$"
    ),
    page: int = Query(1, ge=1),
    limit: int = Query(9, ge=1, le=50),
    db=Depends(get_db),
    user=Depends(get_current_user)
):
    """
    Retrieve paginated tasks with optional status filtering.

    Query Parameters:
        status (str): Task status filter
        page (int): Page number
        limit (int): Items per page

    Access Control:
        Admin only.

    Returns:
        dict: Paginated task data
    """
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
    """
    Retrieve upcoming tasks within a given number of days.

    Query Parameters:
        days (int): Number of upcoming days (1–30)

    Access Control:
        Admin only.

    Returns:
        list[dict]: Upcoming tasks
    """
    return task_controller.get_upcoming_tasks(db, days, user)


@router.get("/count")
def get_count(db=Depends(get_db)):
    """
    Retrieve total number of tasks.

    Returns:
        dict: Task count
    """
    return task_controller.get_count_of_all_tasks(db)


@router.put("/{task_id}")
def update_task(
    task_id: int,
    task: TaskUpdateSchema,
    db=Depends(get_db),
    user=Depends(get_current_user),
):
    """
    Update task details.

    Access Control:
        Admin only.

    Request Body:
        TaskUpdateSchema

    Returns:
        dict: Updated task details
    """
    return task_controller.update_task(db, task_id, task, user)


@router.delete("/{task_id}")
def delete_task(
    task_id: int,
    db=Depends(get_db),
    user=Depends(get_current_user),
):
    """
    Delete a task.

    Access Control:
        Admin only.

    Returns:
        None
    """
    return task_controller.delete_task(db, task_id, user)
