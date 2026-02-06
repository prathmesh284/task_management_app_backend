from pydantic import BaseModel, Field, validator
from datetime import date
from typing import Optional, Literal
import re

# -------- Regex for validate Title --------
TITLE_REGEX = re.compile(r"^[A-Za-z, ]{3,}$")

# -------- Requests --------

class TaskCreateSchema(BaseModel):
    title: str = Field(..., min_length=3)
    description: str | None = None
    assigned_to: int
    due_date: date

    # validating title, it must not contain any special character
    @validator("title")
    def validate_title(cls, v):
        if not TITLE_REGEX.match(v):
            raise ValueError(
                "Title must not contain any Special Character (min 5 chars)"
            )
        return v

    # validating due date, due date must be greater then current date
    @validator("due_date")
    def validate_due_date(cls, v):
        if v <= date.today():
            raise ValueError("Due date must be after today")
        return v



class TaskUpdateSchema(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    due_date: Optional[date] = None


# -------- Responses --------

class TaskResponseSchema(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    status: str
    due_date: Optional[date] = None
    assigned_to: int

class TaskStatusUpdateSchema(BaseModel):
    status: Literal["In Progress", "Completed"]