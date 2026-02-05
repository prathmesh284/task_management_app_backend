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

# Allowed transitions: Pending -> In Progress -> Completed
ALLOWED_TRANSITIONS = {
    "Pending": "In Progress",
    "In Progress": "Completed",
}

def update_task_status(db, task_id: int, new_status: str, current_user):
    task = task_dao.get_task_by_id(db, task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    # Ownership check (employee can update only their task)
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
