import logging
from fastapi import APIRouter
from app.infrastructure.entry_point.dto.user_dto import UserDto
import app.infrastructure.entry_point.handler.user_handler as user_handler

router = APIRouter()

@router.get("/")
def read_root():
    return {"Hello": "World"}

@router.post("/create-user")
def create_user(request: UserDto):
    logging.info(f"Received request tocreate user: {request}")
    return user_handler.create_user(request)