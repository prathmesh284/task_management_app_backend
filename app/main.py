"""
Main Application Entry Point
----------------------------
This file initializes the FastAPI application for the Task Management System.
It configures CORS settings and registers all API route modules.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Importing route modules
from app.routes import auth_routes, task_routes, user_routes, comment_routes


# Create FastAPI application instance
app = FastAPI(
    title="Task Management System",
    description="Backend API for managing users, tasks, and comments"
)


# -----------------------------
# CORS Configuration
# -----------------------------
# Allows the frontend (Vite/React) to communicate with this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",   # Vite development server
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],          # Allow all HTTP methods
    allow_headers=["*"],          # Allow all headers
)


# -----------------------------
# API Route Registration
# -----------------------------
# Authentication-related APIs
app.include_router(auth_routes.router)

# Task management APIs
app.include_router(task_routes.router)

# User-related APIs
app.include_router(user_routes.router)

# Comment-related APIs
app.include_router(comment_routes.router)


# -----------------------------
# Root Endpoint
# -----------------------------
@app.get("/")
def root():
    """
    Root endpoint to verify backend status.

    Returns:
        dict: Status message indicating backend is running.
    """
    return {"status": "Backend running"}
