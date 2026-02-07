from app.queries import task_queries as q

def create_task(db, task):
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
    cur = db.cursor()
    cur.execute(q.GET_TASKS_BY_USER, (user_id,))
    return cur.fetchall()

def get_all_tasks(db):
    cur = db.cursor()
    cur.execute(q.GET_ALL_TASKS)
    return cur.fetchall()

def get_task_by_id(db, task_id: int):
    cur = db.cursor()
    cur.execute(q.GET_TASK_BY_ID, (task_id,))
    return cur.fetchone()

def update_task_status(db, task_id: int, status: str):
    cur = db.cursor()
    cur.execute(q.UPDATE_TASK_STATUS, (status, task_id))
    task = cur.fetchone()
    db.commit()
    return task

def get_tasks_paginated(db, status, limit, offset):
    cur = db.cursor()
    cur.execute(
        q.GET_TASKS_PAGINATED,
        (status, status, limit, offset)
    )
    return cur.fetchall()

def count_tasks(db, status):
    cur = db.cursor()
    cur.execute(
        q.COUNT_TASKS,
        (status, status)
    )
    return cur.fetchone()["count"]

def get_upcoming_tasks(db, days: int):
    cur = db.cursor()
    cur.execute(q.GET_UPCOMING_TASKS, (days,))
    return cur.fetchall()

def get_count(db):
    cur = db.cursor()
    cur.execute(q.COUNT_ALL_TASKS)
    return cur.fetchall()

def update_task(db, task_id, task):
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
    cur = db.cursor()
    cur.execute(q.DELETE_TASK, (task_id,))
    db.commit()