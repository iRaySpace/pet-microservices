from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

from models import EventRequest

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/events")
def post_events(event: EventRequest):
    print('Received event: ', event.eventType)
    requests.post("http://localhost:8000/events", json=event.dict())
    requests.post("http://localhost:8001/events", json=event.dict())
    requests.post("http://localhost:8002/events", json=event.dict())
    return "OK"
