from fastapi import APIRouter, Depends, Query
from typing import List

from app.database import get_db
from app.dependencies import get_current_user
from app.schemas.user import UserResponseSchema
from app.controllers import user_controller

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/", response_model=List[UserResponseSchema])
def get_users(db=Depends(get_db), user=Depends(get_current_user)):
    return user_controller.get_all_users(db, user)

@router.get("/stats")
def get_user_stats(db=Depends(get_db), user=Depends(get_current_user)):
    return user_controller.get_employee_count(db, user)

@router.get("/")
def list_users(role: str | None = Query(None, pattern="^(admin|employee)$"), db=Depends(get_db), user=Depends(get_current_user)):
    return user_controller.get_users(db, role, user)