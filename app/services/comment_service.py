"""
Comment Service Module
----------------------
This module contains business logic related to task comments.
It acts as an intermediary between the API routes and the DAO layer.
"""

from app.dao import comment_dao


def add_comment(db, task_id, comment, user):
    """
    Adds a comment to a specific task.

    Args:
        db: Active database connection
        task_id (int): ID of the task
        comment (str): Comment text
        user (dict): Authenticated user details

    Returns:
        dict: Newly created comment details
    """
    return comment_dao.add_comment(
        db,
        task_id,
        user["id"],
        comment
    )


def get_comment(db, task_id):
    """
    Retrieves all comments associated with a task.

    Args:
        db: Active database connection
        task_id (int): ID of the task

    Returns:
        list[dict]: List of task comments
    """
    return comment_dao.get_comments(db, task_id)
