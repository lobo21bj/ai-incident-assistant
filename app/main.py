from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.routes import router
from app.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(router)