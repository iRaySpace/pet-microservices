from typing import Optional
from pydantic import BaseModel

class ClinicRequest(BaseModel):
    name: str
    description: Optional[str] = None

class Clinic(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

class EventRequest(BaseModel):
    eventType: str
    data: dict
