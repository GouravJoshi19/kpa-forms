from fastapi import FastAPI
from app.routes import wheel_specifications
from app import models
from app.database import engine

models.base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(wheel_specifications.router)