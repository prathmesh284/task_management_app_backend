from app.services import auth_service

def register(db, user):
    auth_service.register_user(db, user)
    return {"message": "User registered successfully"}

def login(db, user):
    token = auth_service.login_user(db, user)
    return {"access_token": token, "token_type": "bearer"}
