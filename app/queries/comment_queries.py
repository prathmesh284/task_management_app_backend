CREATE_COMMENT = """
INSERT INTO task_comments (task_id, user_id, comment)
VALUES (%s, %s, %s)
RETURNING id, comment, created_at;
"""

GET_TASK_COMMENTS = """
SELECT c.id, c.comment, c.created_at, u.name
FROM task_comments c
JOIN users u ON u.id = c.user_id
WHERE c.task_id = %s
ORDER BY c.created_at DESC;
"""