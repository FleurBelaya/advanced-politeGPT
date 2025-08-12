from fastapi import APIRouter
from src.logging_config import logger

router = APIRouter(prefix="/home")

@router.get("/")
def read_root():
    logger.info("Handling request to root endpoint")
    return {"message": "Hello, World!"}

