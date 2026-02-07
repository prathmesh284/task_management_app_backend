from fastapi import FastAPI
from app.routes import auth_routes,task_routes,user_routes,comment_routes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Task Management System")

# CORS CONFIG
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # Vite
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_routes.router)
app.include_router(task_routes.router)
app.include_router(user_routes.router)
app.include_router(comment_routes.router)

@app.get("/")
def root():
    return {"status": "Backend running"}
