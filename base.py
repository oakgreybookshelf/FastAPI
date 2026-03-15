from fastapi import APIRouter, FastAPI
from pydantic import BaseModel
import create_profile

app = FastAPI(
    title="Interactive Dating App",
    description="This is the basis for interacting with a dating application using FastAPI",
    version="1.0.0"
)
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

@app.post("/create_user/")
async def user_profile(user_data: create_profile.CreateProfile):
    '''
    Purpose: This function creates a user's profile.
    Parameters: name, age, pronouns, location
    Example Input:
        {
          "Name": "Kina",
          "Age": 21,
          "Pronouns": "they/she",
          "Location": "Cityville"
        }
    Example Output:
        {
          "Message": "Created User Profile! ",
          "data": { "Name": "Kina",  "Age": 21, "Pronouns": "they/she", "Location": "Cityville"}
        }
    '''    
    name = user_data.name
    age = user_data.age
    pronouns = user_data.pronouns
    location = user_data.location
    return {
        "Message": "Created User Profile! ",
        "Name": name,
        "Age": age,
        "Pronouns": pronouns,
        "Location": location
    }

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
    '''
    uvicorn.run(
        app=demo_app(),
        port=8000,
        reload=False,
        loop="uvloop",
    )
    '''
