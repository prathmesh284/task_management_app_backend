from pydantic import BaseModel
from datetime import date
from typing import Optional

# -------- Requests --------

class TaskCreateSchema(BaseModel):
    title: str
    description: Optional[str] = None
    assigned_to: int
    due_date: date


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
