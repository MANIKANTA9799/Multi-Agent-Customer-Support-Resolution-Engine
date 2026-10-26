from app.agents.base import BaseAgent
from app.models.ticket import Ticket
from openai import OpenAI
from app.models.mesaage import Message
from sqlalchemy.orm import Session
client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
class  TechsupportAgent (BaseAgent):
 def process(self,ticket:Ticket,db:Session):
    messages = [
        {
            "role": "system",
            "content": "You are a helpful tech support AI. Be concise."
        },
        {
            "role": "user",
            "content": f"Ticket Subject: {ticket.subject}"
        }
    ]
    response = client.chat.completions.create(
        model="llama3.1",
        messages=messages #type:ignore
    )    
    content =  str( response.choices[0].message.content)
    
    msg = Message(
    content=content,
    ticket_id=ticket.id,
    sender_type="agent",
)

    db.add(msg)

    return content