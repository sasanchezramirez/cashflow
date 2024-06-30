from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("postgresql://cashflow-db:cashflow2024@db:5432/cashflow")
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_session():
    try:
        session = SessionLocal()
        yield session
    finally:
        session.close()