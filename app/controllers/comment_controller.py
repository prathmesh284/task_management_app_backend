from app.services import comment_service

def add_comment(db, task_id, comment, user):
    return comment_service.add_comment(db, task_id, comment, user)

def get_comment(db, task_id):
    return comment_service.get_comment(db, task_id)