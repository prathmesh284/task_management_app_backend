from app.queries import user_queries as q

def is_email_exists(db, email):
    cur = db.cursor()
    cur.execute(q.CHECK_USER_EMAIL, (email,))
    return cur.fetchone()

def create_user(db, name, email, password, role):
    cur = db.cursor()
    cur.execute(q.INSERT_USER, (name, email, password, role))
    db.commit()

def get_user_by_email(db, email):
    cur = db.cursor()
    cur.execute(q.GET_USER_BY_EMAIL, (email,))
    return cur.fetchone()

def get_user_by_id(db, user_id):
    cur = db.cursor()
    cur.execute(q.GET_USER_BY_ID, (user_id,))
    return cur.fetchone()

def get_all_users(db):
    cur = db.cursor()
    cur.execute(q.GET_ALL_USERS)
    return cur.fetchall()

def get_employee_count(db):
    cur = db.cursor()
    cur.execute(q.GET_EMPLOYEE_COUNT)
    return cur.fetchone()

def get_users_by_role(db, role):
    cur = db.cursor()
    cur.execute(q.GET_USERS_BY_ROLE, (role, role))
    return cur.fetchall()