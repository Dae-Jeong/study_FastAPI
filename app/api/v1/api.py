from fastapi import APIRouter
from app.api.v1.endpoints import todo

api_v1_router = APIRouter()
api_v1_router.include_router(todo.todo_router, prefix="/todo", tags=["todo"])
