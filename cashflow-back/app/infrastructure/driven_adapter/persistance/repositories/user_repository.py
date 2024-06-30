import logging
from sqlalchemy.orm import Session
from app.infrastructure.driven_adapter.persistance.models.user_entity import User_entity

class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_user(self, user: User_entity):
        logging.info(f"Creating user: {user}")
        user = User_entity(user)
        self.session.add(user)
        self.session.commit()
        return user
    
    def get_user(self, email: str):
        return self.session.query(User_entity).filter(User_entity.email == email).first()
