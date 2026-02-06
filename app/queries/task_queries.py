CREATE_TASK = """
INSERT INTO tasks (title, description, assigned_to, due_date, status)
VALUES (%s, %s, %s, %s, 'Pending')
RETURNING id, title, status, assigned_to;
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

GET_TASKS_PAGINATED = """
SELECT
    t.id,
    t.title,
    t.description,
    t.status,
    t.due_date,
    t.assigned_to,
    u.name AS assigned_user_name
FROM tasks t
JOIN users u ON u.id = t.assigned_to
WHERE (%s = 'all' OR t.status = %s)
ORDER BY t.created_at DESC
LIMIT %s OFFSET %s;
"""

COUNT_ALL_TASKS = """
SELECT COUNT(*)
FROM tasks
"""

COUNT_TASKS = """
SELECT COUNT(*)
FROM tasks
WHERE (%s = 'all' OR status = %s);
"""

GET_UPCOMING_TASKS = """
SELECT
    t.id,
    t.title,
    t.description,
    t.status,
    t.due_date,
    t.assigned_to,
    u.name AS assigned_user_name
FROM tasks t
JOIN users u ON u.id = t.assigned_to
WHERE
    t.status IN ('Pending', 'In Progress')
    AND t.due_date >= CURRENT_DATE
    AND t.due_date <= CURRENT_DATE + (%s || ' days')::INTERVAL
ORDER BY t.due_date ASC;
"""
