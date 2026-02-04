from fastapi import HTTPException
from app.dao import user_dao
from app.core.security import hash_password, verify_password, create_access_token

def register_user(db, user):
    role = user.role.lower()   # ← normalize

    if role not in ("admin", "employee"):
        raise HTTPException(status_code=400, detail="Invalid role")

    if user_dao.is_email_exists(db, user.email):
        raise HTTPException(status_code=400, detail="Email already exists")

    user_dao.create_user(
        db,
        user.name,
        user.email,
        hash_password(user.password),
        role
    )

def login_user(db, user):
    db_user = user_dao.get_user_by_email(db, user.email)

    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return create_access_token({
        "user_id": db_user["id"],
        "role": db_user["role"]
    })
