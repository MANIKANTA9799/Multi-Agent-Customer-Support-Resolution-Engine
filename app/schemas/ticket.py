from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class TicketCreate(BaseModel):
    subject:str 
    message :str


class TicketResponse (BaseModel):
    id :UUID
    subject:str 
    status :str 
    created_at : datetime 
    updated_at : datetime 
    model_config = ConfigDict(from_attributes=True)



