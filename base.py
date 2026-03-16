from fastapi import APIRouter, FastAPI
from pydantic import BaseModel
from .routers import filter
import create_profile

app = FastAPI(
    title="Interactive Dating App",
    description="This is the basis for interacting with a dating application using FastAPI",
    version="1.0.0"
)
app.include_router(filter.router)

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
