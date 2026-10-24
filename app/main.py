from fastapi import FastAPI
from app.core.config import settings
from app.api.v1.tickets import router

app = FastAPI(title = settings.project_name)
app.include_router(router= router,prefix="/api/v1/tickets")