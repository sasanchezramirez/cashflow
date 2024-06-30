import app.domain.model.user as User
from app.infrastructure.driven_adapter.persistance.service.persistence import Persistence
from sqlalchemy.orm import Session

class PersistenceGateway:
    def __init__(self, session: Session):
        self.persistence = Persistence(session)

    def create_user(self, user: User):
        return self.persistence.create_user(user)
