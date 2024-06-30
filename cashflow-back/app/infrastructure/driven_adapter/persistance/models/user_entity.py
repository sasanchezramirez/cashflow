from sqlalchemy import Column, Integer, String
from app.infrastructure.driven_adapter.persistance.config.database import Base

class User_entity(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    def __init__(self, user):
        self.email = user.email
        self.password = user.password
