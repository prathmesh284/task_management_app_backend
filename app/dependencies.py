"""
Authentication Dependency Module
--------------------------------
This module handles JWT-based authentication and provides
a dependency to retrieve the currently authenticated user.
"""

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

from app.database import get_db
from app.core.config import SECRET_KEY, ALGORITHM
from app.dao import user_dao


# OAuth2 scheme to extract Bearer token from Authorization header
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db=Depends(get_db)
):
    """
    Retrieves the currently authenticated user based on JWT token.

    This function:
    - Extracts the Bearer token from the request
    - Decodes and validates the JWT
    - Fetches the corresponding user from the database
    - Raises appropriate HTTP errors if authentication fails

    Args:
        token (str): JWT access token extracted from Authorization header
        db: Database connection dependency

    Returns:
        dict: Authenticated user details

    Raises:
        HTTPException: If token is invalid, expired, or user does not exist
    """

    # -----------------------------
    # Decode and validate JWT token
    # -----------------------------
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: int | None = payload.get("user_id")
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )

    # Ensure token contains user identifier
    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token payload"
        )

    # -----------------------------
    # Fetch user from database
    # -----------------------------
    user = user_dao.get_user_by_id(db, user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )

    # -----------------------------
    # Return authenticated user
    # -----------------------------
    return user
