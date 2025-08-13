# from fastapi import APIRouter
# from src.schemas.users_schema import fake_users
# from src.logging_config import logger
#
# router = APIRouter(prefix="/users")
#
# # GET /users
# @router.get("/")
# def view_users():
#     return fake_users  # .json() не нужно, словарь и так вернётся как JSON
#
# # GET /users/{user_id}
# @router.get("/{user_id}")
# def get_user(user_id: int):
#     if user_id in fake_users:
#         return fake_users[user_id]
#     return {"error": "User not found"}
#
# # GET /users?limit=3
# @router.get("/limit")
# def read_limit_users(limit: int = 3):
#     return dict(list(fake_users.items())[:limit])

