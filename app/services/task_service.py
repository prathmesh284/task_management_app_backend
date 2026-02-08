"""
Task Service Module
-------------------
This module contains business logic related to task management.
It enforces role-based access control, workflow rules, and
pagination logic before interacting with the DAO layer.
"""

import math
from fastapi import HTTPException
from app.dao import task_dao


def create_task(db, task, current_user):
    """
    Creates a new task.

    Access Control:
        Only admin users are allowed to create tasks.

    Args:
        db: Active database connection
        task: Task object containing task details
        current_user (dict): Authenticated user details

    Returns:
        dict: Newly created task

    Raises:
        HTTPException: If user is not an admin
    """
    if current_user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")

    return task_dao.create_task(db, task)


def get_my_tasks(db, user):
    """
    Retrieves tasks assigned to the currently logged-in user.

    Args:
        db: Active database connection
        user (dict): Authenticated user details

    Returns:
        list[dict]: List of tasks assigned to the user
    """
    return task_dao.get_tasks_by_user(db, user["id"])


def get_all_tasks(db):
    """
    Retrieves all tasks from the system.

    Args:
        db: Active database connection

    Returns:
        list[dict]: List of all tasks
    """
    return task_dao.get_all_tasks(db)


# Allowed task status transitions
# Pending -> In Progress -> Completed
ALLOWED_TRANSITIONS = {
    "Pending": "In Progress",
    "In Progress": "Completed",
}


def update_task_status(db, task_id: int, new_status: str, current_user):
    """
    Updates the status of a task following defined workflow rules.

    Rules:
        - Only the assigned user can update the task
        - Status transitions must follow the allowed workflow

    Args:
        db: Active database connection
        task_id (int): Task ID
        new_status (str): New task status
        current_user (dict): Authenticated user details

    Returns:
        dict: Updated task details

    Raises:
        HTTPException: If task not found, user not authorized,
                       or invalid status transition
    """
    task = task_dao.get_task_by_id(db, task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    # Ownership validation
    if task["assigned_to"] != current_user["id"]:
        raise HTTPException(status_code=403, detail="Not allowed")

    current_status = task["status"]

    # Workflow validation
    expected_next = ALLOWED_TRANSITIONS.get(current_status)
    if expected_next != new_status:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid status transition: {current_status} → {new_status}"
        )

    return task_dao.update_task_status(db, task_id, new_status)


def get_tasks_paginated(db, status, page, limit, current_user):
    """
    Retrieves paginated tasks with optional status filtering.

    Access Control:
        Only admin users are allowed.

    Args:
        db: Active database connection
        status (str): Task status or 'all'
        page (int): Page number
        limit (int): Number of items per page
        current_user (dict): Authenticated user details

    Returns:
        dict: Paginated task data including items, total count,
              current page, and total pages

    Raises:
        HTTPException: If user is not an admin
    """
    if current_user["role"] != "admin":
        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )

    # Pagination safety checks
    page = max(page, 1)
    limit = max(limit, 1)
    offset = (page - 1) * limit

    total = task_dao.count_tasks(db, status)
    pages = max(math.ceil(total / limit), 1)

    items = task_dao.get_tasks_paginated(
        db=db,
        status=status,
        limit=limit,
        offset=offset
    )

    return {
        "items": items,
        "total": total,
        "page": page,
        "pages": pages
    }


def get_upcoming_tasks(db, days: int, current_user):
    """
    Retrieves upcoming tasks within a specified number of days.

    Access Control:
        Only admin users are allowed.

    Safety:
        Days value is limited between 1 and 30.

    Args:
        db: Active database connection
        days (int): Number of upcoming days
        current_user (dict): Authenticated user details

    Returns:
        list[dict]: List of upcoming tasks

    Raises:
        HTTPException: If user is not an admin
    """
    if current_user["role"] != "admin":
        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )

    days = min(max(days, 1), 30)
    return task_dao.get_upcoming_tasks(db, days)


def get_count(db):
    """
    Retrieves the total number of tasks.

    Args:
        db: Active database connection

    Returns:
        list[dict]: Task count data
    """
    return task_dao.get_count(db)


def update_task(db, task_id, task, user):
    """
    Updates task details.

    Access Control:
        Only admin users are allowed.

    Args:
        db: Active database connection
        task_id (int): Task ID
        task: Task object with updated values
        user (dict): Authenticated user details

    Returns:
        dict: Updated task details

    Raises:
        HTTPException: If user is not an admin
    """
    if user["role"] != "admin":
        raise HTTPException(403, "Admin access required")

    return task_dao.update_task(db, task_id, task)


def delete_task(db, task_id, user):
    """
    Deletes a task from the system.

    Access Control:
        Only admin users are allowed.

    Args:
        db: Active database connection
        task_id (int): Task ID
        user (dict): Authenticated user details

    Returns:
        None

    Raises:
        HTTPException: If user is not an admin
    """
    if user["role"] != "admin":
        raise HTTPException(403, "Admin access required")

    task_dao.delete_task(db, task_id)
