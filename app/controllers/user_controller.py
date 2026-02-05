from app.services import user_service

def get_all_users(db, current_user):
    return user_service.get_all_users(db, current_user)

def get_employee_count(db, current_user):
    return user_service.get_employee_count(db, current_user)