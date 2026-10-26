from app.agents.base import BaseAgent
from app.models.ticket import Ticket
from sqlalchemy.orm import Session
from openai import OpenAI
from app.models.mesaage import Message
import json
def execute_stripe_refund(ticket_id: str) -> str:
    print(f"--- STRIPE API CALLED FOR TICKET {ticket_id} ---")
    return "Refund successful. Transaction ID: txn_98765"

refund_tool = {
    "type": "function",
    "function": {
        "name": "execute_stripe_refund",
        "description": "Executes a monetary refund for a customer ticket via Stripe.",
        "parameters": {
            "type": "object",
            "properties": {
                "ticket_id": {"type": "string", "description": "The UUID of the ticket"}
            },
            "required": ["ticket_id"]
        }
    }
}

class BillingAgent(BaseAgent):
    def __init__(self) -> None:
        super().__init__()
       
    def process(self,ticket: Ticket,db: Session) -> str:
        client = OpenAI(
            base_url="http://localhost:11434/v1",
            api_key="ollama"
        )

        messages = [
            {
                "role": "system",
                "content": "You are a billing agent. If the user asks for a refund, use the refund tool."
            },
            {
                "role": "user",
                "content": f"Ticket Subject: {ticket.subject}"
            }
        ]

        response = client.chat.completions.create(
            model="llama3.1",
            messages=messages,#type:ignore
            tools=[refund_tool]#type:ignore 
        )

        msg = response.choices[0].message

        if msg.tool_calls:
            call = msg.tool_calls[0]

            args = json.loads(call.function.arguments) #type:ignore

            result = execute_stripe_refund(**args)

            content = result
        else:
            content = msg.content

        message = Message(
            content=content,
            ticket_id=ticket.id,
            sender_type="agent"
        )

        db.add(message)

        return str(content)
    

 # here u can see we add but we did not commit becos commiting is the work of the worker otheriwise we will have duplicates 

        
    # here the most importnat thing to keep in mind 
    # is that we put calss thing in init not everthing if we do so putting 
    #everything we have in  process thing we will just ruin the statelessness 