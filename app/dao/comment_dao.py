"""
Comment Data Access Object (DAO)
--------------------------------
This module handles database operations related to
comments added to tasks.
"""

from app.queries import comment_queries as q


def add_comment(db, task_id, user_id, comment):
    """
    Adds a new comment to a task.

    Args:
        db: Active database connection
        task_id (int): ID of the task
        user_id (int): ID of the user adding the comment
        comment (str): Comment text

    Returns:
        dict: Newly created comment details
              (id, comment, created_at)
    """
    cur = db.cursor()
    cur.execute(q.CREATE_COMMENT, (task_id, user_id, comment))
    result = cur.fetchone()
    db.commit()
    return result


def get_comments(db, task_id):
    """
    Retrieves all comments for a specific task.

    Args:
        db: Active database connection
        task_id (int): ID of the task

    Returns:
        list[dict]: List of comments with user names,
                    ordered by most recent first
    """
    cur = db.cursor()
    cur.execute(q.GET_TASK_COMMENTS, (task_id,))
    return cur.fetchall()
