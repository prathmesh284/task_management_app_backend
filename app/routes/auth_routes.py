from fastapi import APIRouter, Depends
from app.database import get_db
from app.schemas.user import UserRegisterSchema, UserLoginSchema
from app.controllers import auth_controller

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
def register(user: UserRegisterSchema, db=Depends(get_db)):
    return auth_controller.register(db, user)

@router.post("/login")
def login(user: UserLoginSchema, db=Depends(get_db)):
    return auth_controller.login(db, user)
