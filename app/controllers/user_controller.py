"""
User Controller Module
----------------------
This module acts as an intermediary between
API routes and the user service layer.
"""

from app.services import user_service


def get_all_users(db, current_user):
    """
    Retrieve all users.

    Delegates:
        user_service.get_all_users

    Args:
        db: Active database connection
        current_user (dict): Authenticated user details

    Returns:
        list[dict]: List of all users
    """
    return user_service.get_all_users(db, current_user)


def get_employee_count(db, current_user):
    """
    Retrieve total employee count.

    Delegates:
        user_service.get_employee_count

    Args:
        db: Active database connection
        current_user (dict): Authenticated user details

    Returns:
        dict: Employee count data
    """
    return user_service.get_employee_count(db, current_user)


def get_users(db, role, current_user):
    """
    Retrieve users filtered by role.

    Delegates:
        user_service.get_users

    Args:
        db: Active database connection
        role (str | None): Role filter
        current_user (dict): Authenticated user details

    Returns:
        list[dict]: List of users matching the role
    """
    return user_service.get_users(
        db=db,
        role=role,
        current_user=current_user
    )
