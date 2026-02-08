"""
User Routes
-----------
This module defines API endpoints related to user management.
All routes are protected and require authentication.
"""

from fastapi import APIRouter, Depends, Query
from typing import List

from app.database import get_db
from app.dependencies import get_current_user
from app.schemas.user import UserResponseSchema
from app.controllers import user_controller


# Router configuration
router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/", response_model=List[UserResponseSchema])
def get_users(
    db=Depends(get_db),
    user=Depends(get_current_user)
):
    """
    Retrieve all users.

    Access Control:
        Admin only.

    Returns:
        List[UserResponseSchema]: List of all users
    """
    return user_controller.get_all_users(db, user)


@router.get("/stats")
def get_user_stats(
    db=Depends(get_db),
    user=Depends(get_current_user)
):
    """
    Retrieve user statistics.

    Currently returns:
        - Total number of employees

    Access Control:
        Admin only.

    Returns:
        dict: User statistics
    """
    return user_controller.get_employee_count(db, user)


@router.get("/filter")
def list_users(
    role: str | None = Query(
        None,
        pattern="^(admin|employee)$"
    ),
    db=Depends(get_db),
    user=Depends(get_current_user)
):
    """
    Retrieve users filtered by role.

    Query Parameters:
        role (str | None): Filter users by role (admin or employee)

    Access Control:
        Admin only.

    Returns:
        list[dict]: List of users matching the role filter
    """
    return user_controller.get_users(db, role, user)
