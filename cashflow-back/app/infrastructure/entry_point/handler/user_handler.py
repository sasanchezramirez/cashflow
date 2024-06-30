import logging
import app.infrastructure.entry_point.dto.generic_response_dto as generic_response_dto
from app.infrastructure.entry_point.dto.user_dto import UserDto
from app.domain.usecase.user_usecase import UserUseCase
from app.infrastructure.driven_adapter.persistance.service.persistence import Persistence

def create_user(user: UserDto, session):
    logging.info(f"Initializing create user handler with user: {user}")
    persistence= Persistence(session)
    user_usecase = UserUseCase(persistence)
    
    response = user_usecase.create_user(user)

    if response:
        status_code = 200
        data = {"response": "User created successfully"}
    else:
        status_code = 500
        data = {"error": "Internal Server Error"}

    response_dto = generic_response_dto.GenericResponseDto(data = data, status_code = status_code)

    logging.info(f"Response: {response_dto}")
    return response_dto.to_response()
