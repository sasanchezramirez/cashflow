from sqlalchemy import Column, Integer, String, Date
from infrastructure.driven_adapter.persistance.config.database import Base

class Expense(Base):
    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    amount = Column(Integer)
    description = Column(String)
    category_id = Column(Integer, index=True)
    priority_id = Column(Integer, index=True)
    date = Column(Date)

