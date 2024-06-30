import app.domain.model.user as User
from app.infrastructure.driven_adapter.persistance.service.persistence import Persistence
from app.infrastructure.driven_adapter.persistance.repositories.user_repository import UserRepository
from app.infrastructure.driven_adapter.persistance.config.database import get_session
from sqlalchemy.orm import Session

class PersistenceGateway:
    def __init__(self, session: Session):
        self.persistence = Persistence(session)
        self.user_repository = UserRepository(session)

    def create_user(self, user: User):
        return self.persistence.create_user( user)
