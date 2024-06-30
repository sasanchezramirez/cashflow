import logging
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.infrastructure.driven_adapter.persistance.config.database import get_session
from app.infrastructure.entry_point.dto.user_dto import UserDto
import app.infrastructure.entry_point.handler.user_handler as user_handler

router = APIRouter()

@router.get("/")
def read_root():
    return {"Hello": "World"}

@router.post("/create-user")
def create_user(request: UserDto, session: Session = Depends(get_session)):
    logging.info(f"Received request tocreate user: {request}")
    return user_handler.create_user(request, session)

@router.get("/get-user")
def get_user(email: str, session: Session = Depends(get_session)):
    logging.info(f"Received request to get user")
    return user_handler.get_user(email, session)