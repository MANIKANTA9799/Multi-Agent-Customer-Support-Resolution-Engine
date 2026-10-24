from typing import Generator
from fastapi import Depends
from sqlalchemy.orm import Session 
from app.core.db import SessionLocal
from app.services.ticket_service import TicketService


def get_db()-> Generator[Session,None,None]:
    db = SessionLocal()
    try : 
        yield db 
    finally:
        db.close()


def get_ticket_service(db : Session = Depends(get_db))->TicketService:
    return TicketService(db)