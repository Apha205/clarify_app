from fastapi import FastAPI
from .api.v1.api_router import api_router
from .db.models import Base
from .db.session import engine

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Clarify Backend", version="1.0.0")

app.include_router(api_router, prefix="/api/v1")