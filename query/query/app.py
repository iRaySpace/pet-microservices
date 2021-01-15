from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from models import EventRequest

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

clinics = []

@app.get("/clinics")
def read_clinics():
    return clinics


@app.post("/events")
def post_events(event: EventRequest):
    if event.eventType == 'CLINIC_CREATED':
        clinics.append(event.data)
    if event.eventType == 'REVIEW_CREATED':
        existing_clinics = list(filter(lambda x: x.get("id") == event.data.get("id"), clinics))
        existing_clinic = existing_clinics[0]
        existing_clinic['comments'] = [
            *existing_clinic.get('comments', []),
            event.data
        ]
    return "OK"