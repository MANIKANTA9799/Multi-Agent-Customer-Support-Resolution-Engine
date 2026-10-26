from fastapi import FastAPI
from app.core.config import settings
from app.api.v1.tickets import router
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Request
from app.api.v1.auth import router as auth_router
import time 



app = FastAPI(title = settings.project_name)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router= router,prefix="/api/v1/tickets")
app.include_router(
    auth_router,
    prefix="/api/v1"
)

@app.middleware("http")
async def middle(request:Request, call_next):
     st = time.time()
     response = await  call_next(request)
     pt =  time.time()-st
     response.headers["Process-Time"] = str(pt)
     return response