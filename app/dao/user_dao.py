"""
User Data Access Object (DAO)
----------------------------
This module contains database operations related to users.
It acts as an interface between the application logic and
the underlying SQL queries.
"""

from app.queries import user_queries as q


def is_email_exists(db, email):
    """
    Checks whether a user email already exists in the database.

    Args:
        db: Active database connection
        email (str): Email address to check

    Returns:
        dict | None: User record if email exists, otherwise None
    """
    cur = db.cursor()
    cur.execute(q.CHECK_USER_EMAIL, (email,))
    return cur.fetchone()


def create_user(db, name, email, password, role):
    """
    Creates a new user in the database.

    Args:
        db: Active database connection
        name (str): User's full name
        email (str): User's email address
        password (str): Hashed password
        role (str): User role (e.g., admin, employee)

    Returns:
        None
    """
    cur = db.cursor()
    cur.execute(q.INSERT_USER, (name, email, password, role))
    db.commit()


def get_user_by_email(db, email):
    """
    Retrieves a user by email address.

    Args:
        db: Active database connection
        email (str): User's email address

    Returns:
        dict | None: User details including id, password, and role
    """
    cur = db.cursor()
    cur.execute(q.GET_USER_BY_EMAIL, (email,))
    return cur.fetchone()


def get_user_by_id(db, user_id):
    """
    Retrieves a user by user ID.

    Args:
        db: Active database connection
        user_id (int): Unique user identifier

    Returns:
        dict | None: User details including id, name, email, and role
    """
    cur = db.cursor()
    cur.execute(q.GET_USER_BY_ID, (user_id,))
    return cur.fetchone()


def get_all_users(db):
    """
    Retrieves all users from the database.

    Admin users are listed first, followed by other users.

    Args:
        db: Active database connection

    Returns:
        list[dict]: List of all user records
    """
    cur = db.cursor()
    cur.execute(q.GET_ALL_USERS)
    return cur.fetchall()


def get_employee_count(db):
    """
    Retrieves the total number of employees.

    Args:
        db: Active database connection

    Returns:
        dict: Count of users with role 'employee'
    """
    cur = db.cursor()
    cur.execute(q.GET_EMPLOYEE_COUNT)
    return cur.fetchone()


def get_users_by_role(db, role):
    """
    Retrieves users filtered by role.

    Args:
        db: Active database connection
        role (str): Role to filter users by

    Returns:
        list[dict]: List of users matching the given role
    """
    cur = db.cursor()
    cur.execute(q.GET_USERS_BY_ROLE, (role, role))
    return cur.fetchall()
