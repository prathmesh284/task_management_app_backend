"""
Comment Schema Definitions
--------------------------
This module defines Pydantic models for validating
comment-related request and response data.
"""

from pydantic import BaseModel, Field
from datetime import datetime


class CommentCreateSchema(BaseModel):
    """
    Schema for creating a new comment.
    """
    comment: str = Field(
        ...,
        min_length=1,
        max_length=500,
        example="Please complete this task by tomorrow."
    )


class CommentResponseSchema(BaseModel):
    """
    Schema for comment response data.
    """
    id: int
    comment: str
    created_at: datetime
    user_name: str

    class Config:
        from_attributes = True
