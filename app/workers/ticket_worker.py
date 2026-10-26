import time 
from app.core.db import SessionLocal
from app.repos.ticket_repo import TicketRepository
import signal
from app.agents.orchestrator import AgentOrchestrator


class TicketWorker:
   def __init__(self) -> None:
      self.is_running = True 
   def stop(self):
       self.is_running = False
   def run(self):
      agent_orch = AgentOrchestrator()
      # this needs to be out of while loop otherwise we will be doing it mutiple times which is unecssary 
      while self.is_running:
            # 1. Open a short-lived database session for THIS specific loop iteration
            with SessionLocal() as db:
                repo = TicketRepository(db)
                
                # 2. Try to claim a ticket using our FOR UPDATE SKIP LOCKED method
                ticket = repo.claim_ticket()
                
                

                if ticket:
                    print(f"Claimed ticket {ticket.id}. Processing...")
                    agent   = agent_orch.get_agent(ticket = ticket)
                    result = agent.process(ticket,db)
                    print(result)
                    ticket.status = 'resolved'
                    db.commit()
                else:
                    # 3. No tickets found. Sleep to prevent 100% CPU usage.
                    time.sleep(2)  

if __name__ == "__main__":
    worker = TicketWorker()

    def handle_signal(signum, frame):
        worker.stop()

    signal.signal(signal.SIGINT, handle_signal)
    signal.signal(signal.SIGTERM, handle_signal)

    worker.run()


# this has nothing to do with this slide but we are basically using idempotent keys to solve double write prob and we dont generate the idempotent keys randomnly they have a relation with the call we making 

