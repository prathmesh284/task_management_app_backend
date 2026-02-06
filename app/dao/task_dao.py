from app.queries import task_queries as q

def create_task(db, title, description, assigned_to, due_date):
    cur = db.cursor()
    cur.execute(q.CREATE_TASK, (title, description, assigned_to, due_date))
    db.commit()

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