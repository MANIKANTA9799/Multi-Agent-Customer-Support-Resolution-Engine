from fastapi import APIRouter,status,Depends
from fastapi import HTTPException
from app.schemas.ticket import TicketCreate,TicketResponse
from sqlalchemy.orm import Session
from app.services.ticket_service import TicketService
from app.api.dependencies import get_ticket_service
from uuid import UUID
from app.models.user import User
from app.core.security import get_current_user
from app.schemas.ticket import TicketDetailResponse
router = APIRouter(
    prefix = "",
    tags = ["Tickets"]
)


@router.post("",response_model=TicketResponse,status_code=status.HTTP_202_ACCEPTED)
def create_ticket(ticket_in : TicketCreate ,service:TicketService=Depends(get_ticket_service)):
     user_id = UUID("12345678-1234-5678-1234-567812345678")
     result = service.create_ticket(
        user_id=user_id,
        ticket_in=ticket_in
    )

     return result


@router.get("/{ticket_id}",response_model=TicketDetailResponse )
def get_ticket(ticket_id:UUID,service:TicketService=Depends(get_ticket_service),current_user: User = Depends(get_current_user)):
     ticket =  service.get_ticket(ticket_id)
     if ticket :
        if ticket.user_id == current_user.id:
            return   ticket
        else :
            raise HTTPException(status_code=403)
     else :
         raise HTTPException(status_code=404)