"""
Comment Controller Module
-------------------------
This module acts as an intermediary between
API routes and the comment service layer.
It forwards requests related to task comments
to the appropriate service functions.
"""

from app.services import comment_service


def add_comment(db, task_id, comment, user):
    """
    Add a comment to a task.

    Delegates:
        comment_service.add_comment

    Args:
        db: Active database connection
        task_id (int): ID of the task
        comment (str): Comment text
        user (dict): Authenticated user details

    Returns:
        dict: Newly created comment details
    """
    return comment_service.add_comment(
        db,
        task_id,
        comment,
        user
    )


def get_comment(db, task_id):
    """
    Retrieve all comments for a task.

    Delegates:
        comment_service.get_comment

    Args:
        db: Active database connection
        task_id (int): ID of the task

    Returns:
        list[dict]: List of comments associated with the task
    """
    return comment_service.get_comment(db, task_id)
