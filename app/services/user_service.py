from fastapi import HTTPException
from app.dao import user_dao

def get_all_users(db, current_user):
    if current_user["role"] != "admin":
        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )

    return user_dao.get_all_users(db)

def get_employee_count(db, current_user):
    if current_user["role"] != "admin":
        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )

    result = user_dao.get_employee_count(db)
    return {"total_employees": result["total_employees"]}

def get_users(db, role, current_user):
    if current_user["role"] != "admin":
        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )

    return user_dao.get_users_by_role(db, role)