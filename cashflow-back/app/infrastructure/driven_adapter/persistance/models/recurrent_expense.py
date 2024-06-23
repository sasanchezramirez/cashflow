from sqlalchemy import Column, Integer, String, Date
from infrastructure.driven_adapter.persistance.config.database import Base

class recurrent_expense(Base):
    __tablename__ = "recurrent_expenses"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    description = Column(String)
    category_id = Column(Integer, index=True)
    priority_id = Column(Integer, index=True)

