import logging
import app.domain.model.user as User
from app.domain.gateway.persistence_gateway import PersistenceGateway

def create_user(user: User):
    logging.info(f"Initializing usecase to create user: {user}")
    persistence_gateway = PersistenceGateway()
    return persistence_gateway.create_user(user)
