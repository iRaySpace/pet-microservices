from pydantic import BaseModel

class EventRequest(BaseModel):
    eventType: str
    data: dict
