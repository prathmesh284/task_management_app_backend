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
