from sqlalchemy import Column, Integer, String, Date
from infrastructure.driven_adapter.persistance.config.database import Base

class Categories_entity(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    budget_id = Column(Integer, index=True)
    description = Column(String)