from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
# from api_v1 import router as router_v1

from src.models import Base, db_helper

from src.routes import home_routes
from src.routes import user_routes

app = FastAPI()
app.include_router(home_routes, tags=['home'])
app.include_router(user_routes, tags=['view_users'])


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield


app = FastAPI(lifespan=lifespan)
# app.include_router(router=router_v1, prefix=settings.api_v1_prefix)
# app.include_router(home_routes)
# app.include_router(user_routes)

if __name__ == '__main__':
    uvicorn.run('src.main:app', reload=True)

