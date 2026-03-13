from fastapi import APIRouter, FastAPI
from pydantic import BaseModel

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

class UserCreate(BaseModel):
    user_id: int
    username: str
@app.post("/create_user/")

async def create_user(user_data: UserCreate):
    user_id = user_data.user_id
    username = user_data.username
    return {
        "msg": "we got data succesfully",
        "user_id": user_id,
        "username": username,
    }

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
