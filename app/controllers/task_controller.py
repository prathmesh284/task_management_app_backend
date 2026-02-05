from app.services import task_service

def create_task(db, task, current_user):
    task_service.create_task(db, task, current_user)
    return {"message": "Task created"}

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