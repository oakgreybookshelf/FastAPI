from pydantic import BaseModel, Field

class CreateProfile(BaseModel):
    """
    - creates user's profile
    """
    name: string
    username: int
    pronouns: string
    location: string
