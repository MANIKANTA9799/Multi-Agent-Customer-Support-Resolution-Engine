from app.schemas.ticket import TicketCreate
from uuid import UUID
from app.models.ticket import Ticket
from sqlalchemy.orm import Session
from app.models.mesaage import Message
from app.repos.ticket_repo import TicketRepository
class TicketService:
    def __init__(self, db:Session) -> None:
        self.db = db 


    def create_ticket(self,user_id:UUID, ticket_in:TicketCreate)->Ticket:
        ticket = Ticket(user_id = user_id,subject = ticket_in.subject)
        self.db.add(ticket)
        self.db.flush()
        message = Message(ticket_id = ticket.id,sender_type='user',content = ticket_in.message)
        self.db.add(message)
        self.db.commit()
        return ticket 
    
    def get_ticket(self,ticket_id):
        tr = TicketRepository(self.db)
        return tr.get_ticket(ticket_id=ticket_id)
"""the two most imp things that u have learned here is that 
1.we dont directly create session we pass in dependency injectio  so opening and clsoing is handles say by fastapi
2. never create any model so that user can modify info regrading id and shit we use jwt for them 
"""
