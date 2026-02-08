"""
Authentication Service Module
-----------------------------
This module contains business logic for user registration
and login. It handles validation, password security,
and JWT access token generation.
"""

from fastapi import HTTPException
from app.dao import user_dao
from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)


def register_user(db, user):
    """
    Registers a new user in the system.

    Validations:
        - Role must be either 'admin' or 'employee'
        - Email must be unique

    Security:
        - Password is hashed before storing in the database

    Args:
        db: Active database connection
        user: User object containing name, email, password, and role

    Returns:
        None

    Raises:
        HTTPException: If role is invalid or email already exists
    """
    # Normalize role input
    role = user.role.lower()

    if role not in ("admin", "employee"):
        raise HTTPException(
            status_code=400,
            detail="Invalid role"
        )

    # Check for existing email
    if user_dao.is_email_exists(db, user.email):
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    # Create user with hashed password
    user_dao.create_user(
        db,
        user.name,
        user.email,
        hash_password(user.password),
        role
    )


def login_user(db, user):
    """
    Authenticates a user and generates an access token.

    Process:
        - Fetch user by email
        - Verify password using bcrypt
        - Generate JWT access token on success

    Args:
        db: Active database connection
        user: User object containing email and password

    Returns:
        str: JWT access token

    Raises:
        HTTPException: If credentials are invalid
    """
    db_user = user_dao.get_user_by_email(db, user.email)

    if not db_user or not verify_password(
        user.password,
        db_user["password"]
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    # Generate JWT token with user identity and role
    return create_access_token({
        "user_id": db_user["id"],
        "role": db_user["role"]
    })
