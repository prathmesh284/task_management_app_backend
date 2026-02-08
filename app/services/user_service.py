"""
User Service Module
-------------------
This module contains business logic related to user operations.
It enforces authorization rules before interacting with the DAO layer.
"""

from fastapi import HTTPException
from app.dao import user_dao


def get_all_users(db, current_user):
    """
    Retrieves all users from the system.

    Access Control:
        Only users with the 'admin' role are allowed.

    Args:
        db: Active database connection
        current_user (dict): Authenticated user details

    Returns:
        list[dict]: List of all users

    Raises:
        HTTPException: If the user is not an admin
    """
    if current_user["role"] != "admin":
        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )

    return user_dao.get_all_users(db)


def get_employee_count(db, current_user):
    """
    Retrieves the total number of employees.

    Access Control:
        Only users with the 'admin' role are allowed.

    Args:
        db: Active database connection
        current_user (dict): Authenticated user details

    Returns:
        dict: Total number of employees

    Raises:
        HTTPException: If the user is not an admin
    """
    if current_user["role"] != "admin":
        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )

    result = user_dao.get_employee_count(db)
    return {"total_employees": result["total_employees"]}


def get_users(db, role, current_user):
    """
    Retrieves users filtered by role.

    Access Control:
        Only users with the 'admin' role are allowed.

    Args:
        db: Active database connection
        role (str): Role to filter users by
        current_user (dict): Authenticated user details

    Returns:
        list[dict]: List of users matching the specified role

    Raises:
        HTTPException: If the user is not an admin
    """
    if current_user["role"] != "admin":
        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )

    return user_dao.get_users_by_role(db, role)
