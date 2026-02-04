from app.services import task_service

def create_task(db, task, current_user):
    task_service.create_task(db, task, current_user)
    return {"message": "Task created"}

def my_tasks(db, current_user):
    return task_service.get_my_tasks(db, current_user)
