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

UPDATE_TASK_STATUS = """
UPDATE tasks
SET status = %s
WHERE id = %s
RETURNING id, title, description, status, due_date, assigned_to;
"""

GET_TASK_BY_ID = """
SELECT id, status, assigned_to
FROM tasks
WHERE id = %s;
"""
