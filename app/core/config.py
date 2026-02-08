"""
Application Configuration Module
--------------------------------
This module loads and stores application-level configuration
values such as database connection details and security settings.
"""

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# -----------------------------
# Database Configuration
# -----------------------------
DATABASE_URL = os.getenv("DATABASE_URL")


# -----------------------------
# Security / Authentication Configuration
# -----------------------------
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"                     # JWT signing algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = 60        # Token validity duration
