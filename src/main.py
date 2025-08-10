from fastapi import FastAPI
import uvicorn
from datetime import date
from pydantic import BaseModel
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


class User(BaseModel):
    name: str
    age: int
    id: int


@app.get("/")
def read_root():
    logger.info("Handling request to root endpoint")
    return {"message": "Hello, World!"}


@app.get("/user")
def valid_user():
    user_data = {
        "id": '1',
        "name": "John Doe"
    }

    user: User = User(**user_data)
    return user


fake_users = {
    1: {"username": "john_doe", "email": "john@example.com"},
    2: {"username": "jane_smith", "email": "jane@example.com"},
    3: {"username": "alice_jones", "email": "alice@example.com"},
    4: {"username": "bob_white", "email": "bob@example.com"},
}


@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id in fake_users:
        return fake_users[user_id]
    return {"error": "User not found"}


@app.get("/users/")
def read_users(limit: int = 3):
    # Ограничиваем количество пользователей, используя параметр limit
    return dict(list(fake_users.items())[:limit])


if __name__ == '__main__':
    uvicorn.run('src.main:app', reload=True)
