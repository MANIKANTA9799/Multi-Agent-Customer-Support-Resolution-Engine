from sqlalchemy import select , orm 
from app.models.ticket import Ticket 
from uuid import UUID


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
    def get_ticket(self,ticket_id:UUID)->Ticket|None:
        stmt = (
            select(Ticket).options(
                orm.joinedload(Ticket.messages)
            ).where(
                Ticket.id == ticket_id
            )


        )
        result =  self.db.execute(stmt)

        return result.unique().scalar_one_or_none()
        
     
