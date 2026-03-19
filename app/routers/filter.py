from fastapi import APIRouter, FastAPI, WebSocket
from pydantic import BaseModel

router = APIRouter(
    prefix="/filter",
    tags=["filter"],
    responses={404: {"description": "Not found"}},
)

@router.get("/filter")
async def read_items(name: Optional[str] = None, age: Optional[int] = None,
                    pronouns: Optional[str] = None, location: Optional[str] = None
                    ):
    """
    - returns 422 Unprocessable Entity error if q is empty
    """
    filters = {}
    if name:
        filters["name"] = name
    if age:
        filters["age"] = age
    if pronouns:
        filters["pronouns"] = pronouns
    if location:
        filters["location"] = location
    return {"results": name, age, pronouns, location}

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")
