from app.dao import comment_dao

def add_comment(db, task_id, comment, user):
    return comment_dao.add_comment(db, task_id, user["id"], comment)

def get_comment(db, task_id):
    return comment_dao.get_comments(db, task_id)