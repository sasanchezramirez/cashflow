import logging
from sqlalchemy.orm import Session
from app.infrastructure.driven_adapter.persistance.models.user_entity import User_entity
from app.infrastructure.driven_adapter.persistance.repositories.user_repository import UserRepository
from app.domain.model.user import User
from app.domain.gateway.persistence_gateway import PersistenceGateway

class Persistence(PersistenceGateway):
    def __init__(self, session: Session):
        logging.info("Initializing persistence")
        self.session = session
        self.user_repository = UserRepository(session)

    def create_user(self, user: User):
        logging.info(f"Creating user: {user}")
        user_entity = User_entity(user)
        logging.info(f"User created with id: {user_entity.id}")
        return self.user_repository.create_user(user_entity)

    def get_user(self, email: str):
        return self.user_repository.get_user(email)
