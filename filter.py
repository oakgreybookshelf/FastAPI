from fastapi import APIRouter, FastAPI, WebSocket
from pydantic import BaseModel

router = APIRouter(
    prefix="/filter",
    tags=["filter"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def read_items():
    return [{"name": "Item 1"}, {"name": "Item 2"}]
    
@router.get("/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id, "name": f"Item {item_id}"}

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")
