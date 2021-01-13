from typing import Optional
from pydantic import BaseModel

class ReviewRequest(BaseModel):
    parent: int
    rating: int
    feedback: Optional[str] = None

class Review(BaseModel):
    id: int
    parent: int
    rating: int
    feedback: Optional[str] = None
