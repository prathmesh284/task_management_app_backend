"""
Task Data Access Object (DAO)
-----------------------------
This module handles all database operations related to tasks.
It provides an abstraction layer between the application logic
and the task-related SQL queries.
"""

from app.queries import task_queries as q


def create_task(db, task):
    """
    Creates a new task in the database.

    Args:
        db: Active database connection
        task: Task object containing title, description,
              assigned_to, and due_date

    Returns:
        dict: Newly created task details
    """
    cur = db.cursor()
    cur.execute(
        q.CREATE_TASK,
        (
            task.title,
            task.description,
            task.assigned_to,
            task.due_date,
        ),
    )
    new_task = cur.fetchone()
    db.commit()
    return new_task


def get_tasks_by_user(db, user_id):
    """
    Retrieves all tasks assigned to a specific user.

    Args:
        db: Active database connection
        user_id (int): User ID

    Returns:
        list[dict]: List of tasks assigned to the user
    """
    cur = db.cursor()
    cur.execute(q.GET_TASKS_BY_USER, (user_id,))
    return cur.fetchall()


def get_all_tasks(db):
    """
    Retrieves all tasks from the database.

    Args:
        db: Active database connection

    Returns:
        list[dict]: List of all tasks
    """
    cur = db.cursor()
    cur.execute(q.GET_ALL_TASKS)
    return cur.fetchall()


def get_task_by_id(db, task_id: int):
    """
    Retrieves a task by its ID.

    Args:
        db: Active database connection
        task_id (int): Task ID

    Returns:
        dict | None: Task details if found
    """
    cur = db.cursor()
    cur.execute(q.GET_TASK_BY_ID, (task_id,))
    return cur.fetchone()


def update_task_status(db, task_id: int, status: str):
    """
    Updates the status of a task.

    Args:
        db: Active database connection
        task_id (int): Task ID
        status (str): New task status

    Returns:
        dict: Updated task details
    """
    cur = db.cursor()
    cur.execute(q.UPDATE_TASK_STATUS, (status, task_id))
    task = cur.fetchone()
    db.commit()
    return task


def get_tasks_paginated(db, status, limit, offset):
    """
    Retrieves tasks with pagination and optional status filtering.

    Args:
        db: Active database connection
        status (str): Task status or 'all'
        limit (int): Number of records to retrieve
        offset (int): Pagination offset

    Returns:
        list[dict]: Paginated list of tasks
    """
    cur = db.cursor()
    cur.execute(
        q.GET_TASKS_PAGINATED,
        (status, status, limit, offset)
    )
    return cur.fetchall()


def count_tasks(db, status):
    """
    Counts tasks based on status filter.

    Args:
        db: Active database connection
        status (str): Task status or 'all'

    Returns:
        int: Total number of tasks
    """
    cur = db.cursor()
    cur.execute(
        q.COUNT_TASKS,
        (status, status)
    )
    return cur.fetchone()["count"]


def get_upcoming_tasks(db, days: int):
    """
    Retrieves tasks due within the specified number of days.

    Args:
        db: Active database connection
        days (int): Number of upcoming days

    Returns:
        list[dict]: List of upcoming tasks
    """
    cur = db.cursor()
    cur.execute(q.GET_UPCOMING_TASKS, (days,))
    return cur.fetchall()


def get_count(db):
    """
    Retrieves the total count of all tasks.

    Args:
        db: Active database connection

    Returns:
        list[dict]: Total task count
    """
    cur = db.cursor()
    cur.execute(q.COUNT_ALL_TASKS)
    return cur.fetchall()


def update_task(db, task_id, task):
    """
    Updates task details such as title, description,
    assigned user, and due date.

    Args:
        db: Active database connection
        task_id (int): Task ID
        task: Task object with updated values

    Returns:
        dict: Updated task details
    """
    cur = db.cursor()
    cur.execute(
        q.UPDATE_TASK,
        (
            task.title,
            task.description,
            task.assigned_to,
            task.due_date,
            task_id,
        ),
    )
    updated = cur.fetchone()
    db.commit()
    return updated


def delete_task(db, task_id):
    """
    Deletes a task from the database.

    Args:
        db: Active database connection
        task_id (int): Task ID

    Returns:
        None
    """
    cur = db.cursor()
    cur.execute(q.DELETE_TASK, (task_id,))
    db.commit()
