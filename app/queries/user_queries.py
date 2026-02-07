CHECK_USER_EMAIL = """
SELECT id FROM users WHERE email = %s
"""

INSERT_USER = """
INSERT INTO users (name, email, password, role)
VALUES (%s, %s, %s, %s)
"""

GET_USER_BY_EMAIL = """
SELECT id, password, role FROM users WHERE email = %s
"""

GET_USER_BY_ID = """
SELECT id, name, email, role FROM users WHERE id = %s
"""

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
# WHERE role = %s
WHERE role = %s
ORDER BY name ASC,id ASC;
"""

GET_EMPLOYEE_COUNT = """
SELECT COUNT(*) AS total_employees
FROM users
WHERE role = 'employee';
"""
