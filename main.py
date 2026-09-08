from fastapi import FastAPI

from app.config import settings
from app.database import engine,Base
from app.routers import health_check
from app.routers import process
from app.routers import dataset

app = FastAPI(
    title=settings.APP_TITLE,
    version=settings.APP_VERSION
)


Base.metadata.create_all(bind=engine)


app.include_router(health_check.router)
app.include_router(process.router)
app.include_router(dataset.router)