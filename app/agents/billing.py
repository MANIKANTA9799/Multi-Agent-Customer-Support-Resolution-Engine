from app.agents.base import BaseAgent
from app.models.ticket import Ticket
from sqlalchemy.orm import Session
from app.models.mesaage import Message
class BillingAgent(BaseAgent):
    def __init__(self) -> None:
        super().__init__()
       
    def process(self,ticket:Ticket,db:Session):
        message = Message()
        message.ticket_id = ticket.id
        message.sender_type = "agent"
        message.content = "Processed refund via stripe"
        db.add(message)

        return message.content
    
        
    # here the most importnat thing to keep in mind 
    # is that we put calss thing in init not everthing if we do so putting 
    #everything we have in  process thing we will just ruin the statelessness 