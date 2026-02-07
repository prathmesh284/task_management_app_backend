from fastapi import APIRouter, Depends
from app.database import get_db
from app.dependencies import get_current_user
from app.schemas.comment import CommentCreateSchema
from app.controllers import comment_controller

router = APIRouter(prefix="/tasks", tags=["Comments"])

@router.post("/{task_id}/comments")
def add_comment(
    task_id: int,
    body: CommentCreateSchema,
    db=Depends(get_db),
    user=Depends(get_current_user),
):
    return comment_controller.add_comment(db, task_id, body.comment, user)


@router.get("/{task_id}/comments")
def get_comments(
    task_id: int,
    db=Depends(get_db),
    user=Depends(get_current_user),
):
    return comment_controller.get_comment(db, task_id)
