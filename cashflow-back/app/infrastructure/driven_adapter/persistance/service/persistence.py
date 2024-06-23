import logging
from sqlalchemy.orm import Session
from infrastructure.driven_adapter.persistance.model.user import User
from infrastructure.driven_adapter.persistance.repositories.user_repository import UserRepository

class Persistence:
    def __init__(self, session: Session):
        logging.info("Initializing persistence")
        self.session = session
        self.user_repository = UserRepository(session)

    def create_user(self, name: str, email: str, password: str):
        logging.info("Creating user")
        user = User(email=email, password=password)
        logging.info(f"User created with id: {user.id}")
        return self.user_repository.create_user(user)

    def get_user(self, email: str):
        return self.user_repository.get_user(email)
