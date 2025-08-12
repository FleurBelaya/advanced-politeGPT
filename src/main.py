from fastapi import FastAPI
import uvicorn
from src.routes.home_page import router as home_routes
from src.routes.user_view import router as user_routes

app = FastAPI()
app.include_router(home_routes, tags=['home'])
app.include_router(user_routes, tags=['view_users'])


from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == '__main__':
    uvicorn.run('src.main:app', reload=True)

