"""
User Schema Definitions
-----------------------
This module defines Pydantic models for validating
user-related request and response data.
"""

from pydantic import BaseModel, EmailStr


# -----------------------------
# Request Schemas
# -----------------------------

class UserRegisterSchema(BaseModel):
    """
    Schema for user registration requests.
    """
    name: str
    email: EmailStr
    password: str
    role: str   # Allowed values: admin / employee


class UserLoginSchema(BaseModel):
    """
    Schema for user login requests.
    """
    email: EmailStr
    password: str


# -----------------------------
# Response Schemas
# -----------------------------

class UserResponseSchema(BaseModel):
    """
    Schema for user response data.
    """
    id: int
    name: str
    email: EmailStr
    role: str
