from abc import ABC, abstractmethod
from app.domain.model.user import User

class PersistenceGateway(ABC):
    @abstractmethod
    def create_user(self, user: User):
        pass

    @abstractmethod
    def get_user(self, email: str):
        pass


