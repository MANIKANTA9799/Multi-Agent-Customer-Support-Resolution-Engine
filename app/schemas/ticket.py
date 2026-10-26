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


class MessageResponse(BaseModel):
   id :UUID
   sender_type: str 
   content : str 
   created_at : datetime 
   model_config = ConfigDict(from_attributes=True)

class TicketDetailResponse(BaseModel):
   id :UUID
   subject : str 
   status :str 
   messages : list[MessageResponse]
   model_config = ConfigDict(from_attributes=True)
   
   

   """When creating this Pydantic model, allow me to read values from an object's attributes, not just from a dictionary."""
    # the reason is we will read from db objects so to do that we do this



