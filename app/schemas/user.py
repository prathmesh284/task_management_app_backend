from pydantic import BaseModel, EmailStr

# -------- Requests --------

class UserRegisterSchema(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: str  # admin / employee


class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str


# -------- Responses --------

class UserResponseSchema(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: str
