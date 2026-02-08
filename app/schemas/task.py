"""
Task Schema Definitions
-----------------------
This module defines Pydantic models for validating
task-related request and response data.
"""

from pydantic import BaseModel, Field, validator
from datetime import date, datetime
from typing import Optional, Literal
import re


# -----------------------------
# Title Validation Regex
# -----------------------------
# Allows alphabets, spaces, and commas only (minimum length: 3)
TITLE_REGEX = re.compile(r"^[A-Za-z, ]{3,}$")


# -----------------------------
# Request Schemas
# -----------------------------

class TaskCreateSchema(BaseModel):
    """
    Schema for creating a new task.
    """
    title: str = Field(..., min_length=3)
    description: Optional[str] = None
    assigned_to: int
    due_date: date

    @validator("title")
    def validate_title(cls, v):
        """
        Validates task title.

        Rules:
            - Must contain only alphabets, spaces, or commas
            - Must be at least 3 characters long
        """
        if not TITLE_REGEX.match(v):
            raise ValueError(
                "Title must not contain any special characters (min 3 chars)"
            )
        return v

    @validator("due_date")
    def validate_due_date(cls, v):
        """
        Validates task due date.

        Rule:
            - Due date must be later than the current date
        """
        if v <= date.today():
            raise ValueError("Due date must be after today")
        return v


class TaskUpdateSchema(BaseModel):
    """
    Schema for updating task details.
    """
    title: str
    description: Optional[str] = None
    assigned_to: int
    due_date: date


# -----------------------------
# Response Schemas
# -----------------------------

class TaskResponseSchema(BaseModel):
    """
    Schema for task response data.
    """
    id: int
    title: str
    description: Optional[str] = None
    status: str
    due_date: Optional[date] = None
    assigned_to: int
    created_at: datetime


class TaskStatusUpdateSchema(BaseModel):
    """
    Schema for updating task status.
    """
    status: Literal["In Progress", "Completed"]