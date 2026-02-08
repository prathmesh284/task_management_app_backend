"""
Authentication Controller Module
--------------------------------
This module acts as an intermediary between
authentication routes and the authentication service layer.
"""

from app.services import auth_service


def register(db, user):
    """
    Register a new user.

    Delegates:
        auth_service.register_user

    Args:
        db: Active database connection
        user: User registration data

    Returns:
        dict: Success message
    """
    auth_service.register_user(db, user)
    return {"message": "User registered successfully"}


def login(db, user):
    """
    Authenticate a user and return an access token.

    Delegates:
        auth_service.login_user

    Args:
        db: Active database connection
        user: User login credentials

    Returns:
        dict: Access token and token type
    """
    token = auth_service.login_user(db, user)
    return {
        "access_token": token,
        "token_type": "bearer"
    }
