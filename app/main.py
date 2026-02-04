from fastapi import FastAPI
from app.routes import auth_routes,task_routes

app = FastAPI(title="Task Management System")

app.include_router(auth_routes.router)
app.include_router(task_routes.router)

@app.get("/")
def root():
    return {"status": "Backend running"}
