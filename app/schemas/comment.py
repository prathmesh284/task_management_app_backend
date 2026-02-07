from pydantic import BaseModel, Field
from datetime import datetime

class CommentCreateSchema(BaseModel):
    comment: str = Field(
        ...,
        min_length=1,
        max_length=500,
        example="Please complete this task by tomorrow."
    )

class CommentResponseSchema(BaseModel):
    id: int
    comment: str
    created_at: datetime
    user_name: str

    class Config:
        from_attributes = True
