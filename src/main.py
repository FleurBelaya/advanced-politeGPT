from fastapi import FastAPI
import uvicorn
from datetime import date
from pydantic import BaseModel
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/")
def read_root():
    logger.info("Handling request to root endpoint")
    return {"message": "Hello, World!"}


@app.get("/custom")
def read_custom_message():
    return {"message": "This is a custom message!"}


if __name__ == '__main__':
    uvicorn.run(app,
                host='127.0.0.1',
                port=8000)
