import logging
from fastapi import FastAPI
from sqlalchemy.orm import Session
from app.infrastructure.driven_adapter.persistance.config.database import get_session, Base, engine
from app.infrastructure.entry_point.routes import router
from app.infrastructure.driven_adapter.persistance.models.user import User

def create_app() -> FastAPI:
    app = FastAPI(title="CashFLow", version="0.1")
    app.include_router(router)
    return app

app = create_app()


Base.metadata.create_all(bind=engine)


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
    
