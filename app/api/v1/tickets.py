from fastapi import APIRouter,status,Depends
from app.schemas.ticket import TicketCreate,TicketResponse
from sqlalchemy.orm import Session
from app.services.ticket_service import TicketService
from app.api.dependencies import get_ticket_service
from uuid import UUID
router = APIRouter(
    prefix = "/",
    tags = ["Tickets"]
)


@router.post("/create_ticket",response_model=TicketResponse,status_code=status.HTTP_202_ACCEPTED)
def create_ticket(ticket_in : TicketCreate ,service:TicketService=Depends(get_ticket_service)):
     user_id = UUID("12345678-1234-5678-1234-567812345678")
     result = service.create_ticket(
        user_id=user_id,
        ticket_in=ticket_in
    )

     return result
