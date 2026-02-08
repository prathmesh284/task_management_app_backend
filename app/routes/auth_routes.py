"""
Authentication Routes
---------------------
This module defines API endpoints for user registration
and login. It handles request validation and delegates
authentication logic to the auth controller.
"""

from fastapi import APIRouter, Depends
from app.database import get_db
from app.schemas.user import (
    UserRegisterSchema,
    UserLoginSchema
)
from app.controllers import auth_controller


# Router configuration
router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/register")
def register(
    user: UserRegisterSchema,
    db=Depends(get_db)
):
    """
    Register a new user.

    Request Body:
        UserRegisterSchema

    Process:
        - Validates user input
        - Checks role and email uniqueness
        - Hashes password before saving

    Returns:
        None / Success message
    """
    return auth_controller.register(db, user)


@router.post("/login")
def login(
    user: UserLoginSchema,
    db=Depends(get_db)
):
    """
    Authenticate a user and generate an access token.

    Request Body:
        UserLoginSchema

    Process:
        - Verifies user credentials
        - Generates JWT access token on success

    Returns:
        str: JWT access token
    """
    return auth_controller.login(db, user)
