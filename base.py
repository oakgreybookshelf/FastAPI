from fastapi import APIRouter, FastAPI

app = FastAPI()
# Create a router instance
router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)
# Define routes on the router
@router.get("/")
async def read_items():
    return [{"name": "Item 1"}, {"name": "Item 2"}]
@router.get("/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id, "name": f"Item {item_id}"}
# Include the router in the app
app.include_router(router)
