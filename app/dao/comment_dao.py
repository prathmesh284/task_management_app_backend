from app.queries import comment_queries as q


def add_comment(db, task_id, user_id, comment):
    cur = db.cursor()
    cur.execute(q.CREATE_COMMENT, (task_id, user_id, comment))
    result = cur.fetchone()
    db.commit()
    return result


def get_comments(db, task_id):
    cur = db.cursor()
    cur.execute(q.GET_TASK_COMMENTS, (task_id,))
    return cur.fetchall()
