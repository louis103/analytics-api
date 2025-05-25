from fastapi import APIRouter
from .schema import EventSchema

router = APIRouter()


# /api/events/
@router.get("/")
def read_events():
    # A bunch of items (example)
    return {
        "results": [1,2,3]
    }

@router.get("/{event_id}")
def get_event(event_id: int) -> EventSchema:
    # Single row (example)
    return {"id": event_id}