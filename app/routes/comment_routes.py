"""
Comment Routes
--------------
This module defines API endpoints for managing comments
associated with tasks.
"""

from fastapi import APIRouter, Depends
from app.database import get_db
from app.dependencies import get_current_user
from app.schemas.comment import CommentCreateSchema
from app.controllers import comment_controller


# Router configuration
router = APIRouter(
    prefix="/tasks",
    tags=["Comments"]
)


@router.post("/{task_id}/comments")
def add_comment(
    task_id: int,
    body: CommentCreateSchema,
    db=Depends(get_db),
    user=Depends(get_current_user),
):
    """
    Add a new comment to a task.

    Path Parameters:
        task_id (int): ID of the task

    Request Body:
        CommentCreateSchema

    Authentication:
        Required (any authenticated user)

    Returns:
        dict: Newly created comment details
    """
    return comment_controller.add_comment(
        db,
        task_id,
        body.comment,
        user
    )


@router.get("/{task_id}/comments")
def get_comments(
    task_id: int,
    db=Depends(get_db),
    user=Depends(get_current_user),
):
    """
    Retrieve all comments for a task.

    Path Parameters:
        task_id (int): ID of the task

    Authentication:
        Required (any authenticated user)

    Returns:
        list[dict]: List of comments for the task
    """
    return comment_controller.get_comment(db, task_id)
