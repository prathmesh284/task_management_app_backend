"""
Database Connection Module
--------------------------
This module provides a reusable database connection dependency
for interacting with the PostgreSQL database using psycopg.
"""

import psycopg
from psycopg.rows import dict_row
from app.core.config import DATABASE_URL


def get_db():
    """
    Creates and yields a PostgreSQL database connection.

    This function is designed to be used as a FastAPI dependency.
    It provides a database connection for the duration of a request
    and ensures that the connection is properly closed afterward.

    Yields:
        psycopg.Connection: Active PostgreSQL database connection
                            with rows returned as dictionaries.
    """
    # Establish database connection using configured database URL
    conn = psycopg.connect(
        DATABASE_URL,
        row_factory=dict_row  # Return query results as dictionaries
    )

    try:
        # Provide the connection to the request handler
        yield conn
    finally:
        # Ensure the connection is closed after request completion
        conn.close()
