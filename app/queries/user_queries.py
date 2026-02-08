"""
User SQL Query Definitions
--------------------------
This module contains reusable SQL queries related to
user management operations in the Task Management System.
"""

# -----------------------------
# User Existence Checks
# -----------------------------
CHECK_USER_EMAIL = """
SELECT id
FROM users
WHERE email = %s
"""


# -----------------------------
# User Creation
# -----------------------------
INSERT_USER = """
INSERT INTO users (name, email, password, role)
VALUES (%s, %s, %s, %s)
"""


# -----------------------------
# User Retrieval Queries
# -----------------------------
GET_USER_BY_EMAIL = """
SELECT id, password, role
FROM users
WHERE email = %s
"""

GET_USER_BY_ID = """
SELECT id, name, email, role
FROM users
WHERE id = %s
"""


# -----------------------------
# User Listing Queries
# -----------------------------
GET_ALL_USERS = """
SELECT id, name, email, role
FROM users
ORDER BY
  CASE
    WHEN role = 'admin' THEN 1
    ELSE 2
  END,
  name;
"""

GET_USERS_BY_ROLE = """
SELECT id, name, email, role
FROM users
WHERE role = %s
ORDER BY name ASC, id ASC;
"""


# -----------------------------
# User Statistics Queries
# -----------------------------
GET_EMPLOYEE_COUNT = """
SELECT COUNT(*) AS total_employees
FROM users
WHERE role = 'employee';
"""
