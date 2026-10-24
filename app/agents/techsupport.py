from app.agents.base import BaseAgent
from app.models.ticket import Ticket
from sqlalchemy.orm import Session
class  TechsupportAgent (BaseAgent):
    def process(self,ticket:Ticket,db:Session):
        return "Sent troubleshooting steps"