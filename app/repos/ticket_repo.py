from sqlalchemy import select 
from app.models.ticket import Ticket 



class TicketRepository:
    def __init__(self,db):
       self.db = db 
    def claim_ticket(self) :
     query = (
        select(Ticket).where(Ticket.status=="queued").with_for_update(skip_locked=True).limit(1) 
        )
     ticket = self.db.scalars(query).first()
     if ticket:
            ticket.status = "processing"
            ticket.assigned_to = "Worker_A"

            self.db.commit()

            return ticket

     return None
     
