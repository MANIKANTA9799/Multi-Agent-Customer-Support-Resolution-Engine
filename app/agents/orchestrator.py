from app.agents.base import BaseAgent
from app.agents.billing import BillingAgent
from app.agents.techsupport import TechsupportAgent
from app.models.ticket import Ticket

class AgentOrchestrator:

    def get_agent(self, ticket: Ticket) -> BaseAgent:
        subject = ticket.subject.lower()

        if "refund" in subject or "charge" in subject:
            return BillingAgent()

        return TechsupportAgent()