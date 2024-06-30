from app.domain.gateway.persistence_gateway import PersistenceGateway
from app.domain.model.user import User

class UserUseCase:
    def __init__(self, persistence_gateway: PersistenceGateway):
        self.persistence_gateway = persistence_gateway

    def create_user(self, user: User):
        return self.persistence_gateway.create_user(user)
