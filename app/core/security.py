"""
Security Utility Module
-----------------------
This module provides helper functions for:
- Password hashing and verification
- JWT access token generation
"""

from datetime import datetime, timedelta
from jose import jwt
import bcrypt

from app.core.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES


def hash_password(password: str) -> str:
    """
    Hashes a plain-text password using bcrypt.

    Args:
        password (str): User's plain-text password

    Returns:
        str: Securely hashed password
    """
    hashed = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    )
    return hashed.decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifies a plain-text password against a hashed password.

    Args:
        plain_password (str): User-entered password
        hashed_password (str): Stored bcrypt hashed password

    Returns:
        bool: True if password matches, otherwise False
    """
    return bcrypt.checkpw(
        plain_password.encode("utf-8"),
        hashed_password.encode("utf-8")
    )


def create_access_token(data: dict):
    """
    Creates a JWT access token with an expiration time.

    Args:
        data (dict): Payload data to encode in the token
                     (e.g., user_id)

    Returns:
        str: Encoded JWT access token
    """
    # Copy payload data to avoid modifying original dictionary
    to_encode = data.copy()

    # Set token expiration time
    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode.update({"exp": expire})

    # Encode and return JWT
    return jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
