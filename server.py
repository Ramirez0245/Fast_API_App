from fastapi import FastAPI, APIRouter
from app.routes.user import route_user

app = FastAPI()

app.include_router(route_user)  # Creat user


