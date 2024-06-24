from sqlalchemy import Column, Integer, String, Date
from app.infrastructure.driven_adapter.persistance.config.database import Base

class Budgets_entity(Base):
    __tablename__ = "budgets"
    id = Column(Integer, primary_key=True, index=True)
    weekly_amount = Column(Integer)
    monthly_amount = Column(Integer)