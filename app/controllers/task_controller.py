"""
Task Controller Module
----------------------
This module acts as a bridge between the API routes
and the task service layer. It delegates request handling
to the appropriate service functions.
"""

from app.services import task_service


def create_task(db, task, current_user):
    """
    Create a new task.

    Delegates:
        task_service.create_task

    Args:
        db: Active database connection
        task: Task creation data
        current_user (dict): Authenticated user details

    Returns:
        dict: Newly created task
    """
    return task_service.create_task(db, task, current_user)


def my_tasks(db, current_user):
    """
    Retrieve tasks assigned to the current user.

    Delegates:
        task_service.get_my_tasks

    Args:
        db: Active database connection
        current_user (dict): Authenticated user details

    Returns:
        list[dict]: User's assigned tasks
    """
    return task_service.get_my_tasks(db, current_user)


def all_tasks(db):
    """
    Retrieve all tasks (utility/testing purpose).

    Delegates:
        task_service.get_all_tasks

    Args:
        db: Active database connection

    Returns:
        list[dict]: List of all tasks
    """
    return task_service.get_all_tasks(db)


def update_task_status(db, task_id, payload, current_user):
    """
    Update the status of a task.

    Delegates:
        task_service.update_task_status

    Args:
        db: Active database connection
        task_id (int): Task ID
        payload: Status update payload
        current_user (dict): Authenticated user details

    Returns:
        dict: Updated task details
    """
    return task_service.update_task_status(
        db=db,
        task_id=task_id,
        new_status=payload.status,
        current_user=current_user
    )


def get_tasks_paginated(db, status, page, limit, current_user):
    """
    Retrieve paginated tasks with optional status filtering.

    Delegates:
        task_service.get_tasks_paginated

    Args:
        db: Active database connection
        status (str): Task status filter
        page (int): Page number
        limit (int): Items per page
        current_user (dict): Authenticated user details

    Returns:
        dict: Paginated task data
    """
    return task_service.get_tasks_paginated(
        db=db,
        status=status,
        page=page,
        limit=limit,
        current_user=current_user
    )


def get_upcoming_tasks(db, days, current_user):
    """
    Retrieve upcoming tasks within a given number of days.

    Delegates:
        task_service.get_upcoming_tasks

    Args:
        db: Active database connection
        days (int): Number of upcoming days
        current_user (dict): Authenticated user details

    Returns:
        list[dict]: Upcoming tasks
    """
    return task_service.get_upcoming_tasks(
        db=db,
        days=days,
        current_user=current_user
    )


def get_count_of_all_tasks(db):
    """
    Retrieve the total number of tasks.

    Delegates:
        task_service.get_count

    Args:
        db: Active database connection

    Returns:
        dict: Task count data
    """
    return task_service.get_count(db)


def update_task(db, task_id, task, user):
    """
    Update task details.

    Delegates:
        task_service.update_task

    Args:
        db: Active database connection
        task_id (int): Task ID
        task: Task update data
        user (dict): Authenticated user details

    Returns:
        dict: Updated task details
    """
    return task_service.update_task(db, task_id, task, user)


def delete_task(db, task_id, user):
    """
    Delete a task.

    Delegates:
        task_service.delete_task

    Args:
        db: Active database connection
        task_id (int): Task ID
        user (dict): Authenticated user details

    Returns:
        dict: Confirmation message
    """
    task_service.delete_task(db, task_id, user)
    return {"message": "Task deleted"}
