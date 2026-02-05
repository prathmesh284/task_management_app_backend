from fastapi import HTTPException
from app.dao import task_dao

def create_task(db, task, current_user):
    if current_user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")

    task_dao.create_task(
        db,
        task.title,
        task.description,
        task.assigned_to,
        task.due_date
    )

def get_my_tasks(db, user):
    return task_dao.get_tasks_by_user(db, user["id"])

def get_all_tasks(db):
    return task_dao.get_all_tasks(db)