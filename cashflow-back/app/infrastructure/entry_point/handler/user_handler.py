import logging
from app.infrastructure.entry_point.dto.user_dto import UserDto
import app.domain.usecase.user_usecase as user_usecase
import app.infrastructure.entry_point.dto.generic_response_dto as generic_response_dto

def create_user(user: UserDto):
    logging.info(f"Initializing create user handler with user: {user}")

    
    response = user_usecase.create_user(user)

    if response:
        status_code = 200
        data = {"response": "Was able to save the poop times"}
    else:
        status_code = 500
        data = {"error": "Internal Server Error"}

    response_dto = generic_response_dto.GenericResponseDto(data = data, status_code = status_code)

    logging.info(f"Response: {response_dto}")
    return response_dto.to_response()
