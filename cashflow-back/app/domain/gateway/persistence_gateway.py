import app.infrastructure.driven_adapter.persistance.service.persistence as persistence
import app.domain.model.user as User

class PersistenceGateway:
    def __init__(self):
        self.persistence = persistence

    def create_user(self, user: User):
        return self.persistence.create_user(user)

 