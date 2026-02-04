CREATE_TASK = """
INSERT INTO tasks (title, description, assigned_to, due_date)
VALUES (%s, %s, %s, %s)
"""

GET_TASKS_BY_USER = """
SELECT * FROM tasks WHERE assigned_to = %s
"""

GET_ALL_TASKS = """
SELECT * FROM tasks
"""
