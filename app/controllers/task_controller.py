from app.services import task_service

def create_task(db, task, current_user):
    return task_service.create_task(db, task, current_user)

def my_tasks(db, current_user):
    return task_service.get_my_tasks(db, current_user)

def all_tasks(db):
    return task_service.get_all_tasks(db) 

def update_task_status(db, task_id, payload, current_user):
    return task_service.update_task_status(
        db=db,
        task_id=task_id,
        new_status=payload.status,
        current_user=current_user
    )

def get_tasks_paginated(db, status, page, limit, current_user):
    return task_service.get_tasks_paginated(
        db=db,
        status=status,
        page=page,
        limit=limit,
        current_user=current_user
    )

def get_upcoming_tasks(db, days, current_user):
    return task_service.get_upcoming_tasks(
        db=db,
        days=days,
        current_user=current_user
    )

def get_count_of_all_tasks(db):
    return task_service.get_count(db)

def update_task(db, task_id, task, user):
    return task_service.update_task(db, task_id, task, user)

def delete_task(db, task_id, user):
    task_service.delete_task(db, task_id, user)
    return {"message": "Task deleted"}