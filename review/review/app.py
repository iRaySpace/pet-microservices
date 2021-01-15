from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import requests

from models import Review, ReviewRequest, EventRequest

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

reviews = []
reviews_last_id = 0

@app.get("/reviews")
def read_reviews():
    return reviews


@app.get("/reviews/{id}", response_model=List[Review])
def read_review(id: int):
    return list(filter(lambda x: x.parent == id, reviews))


@app.post("/reviews", response_model=Review)
def create_review(review: ReviewRequest):
    global reviews_last_id
    new_review = Review(**review.dict(), id=reviews_last_id)
    reviews.append(new_review)
    reviews_last_id = reviews_last_id + 1
    _post_to_eventbus("REVIEW_CREATED", new_review)
    return new_review


@app.post("/events")
def post_events(event: EventRequest):
    print('review', event)
    return "OK"


def _post_to_eventbus(event_type, data_model):
    requests.post("http://localhost:8010/events", json={
        "eventType": event_type,
        "data": data_model.dict(),
    })
