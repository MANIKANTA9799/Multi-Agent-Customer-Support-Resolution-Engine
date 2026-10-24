from abc import ABC , abstractmethod
from app.models.ticket import Ticket
from sqlalchemy.orm import Session
class BaseAgent(ABC):
    @abstractmethod
    def process(self,ticket:Ticket, db :Session)->str :
      pass
