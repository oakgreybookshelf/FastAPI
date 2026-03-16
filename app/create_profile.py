from pydantic import BaseModel, Field

class CreateProfile(BaseModel):
    """
    - creates user's profile
    """
    name: string
    username: int
    pronouns: string
    location: string


class CreateProfile(BaseModel):
    """
    - creates user's profile
    """
    def __init__(self, name: str, age: int, pronouns: string | None, location: string):
        self.name = string
        self.age = int
        self.pronouns = string
        self.location = string

    self.save_profile(name, age, pronouns, location)

    def save_profile(n, a, p, l):
        """
        - saves user's profile to text file
        """
        file = open("profiles.txt", "a")
        file.write(str(n, a, p, l))
        file.close()
        return

    def delete_profile(n, a, p, l):
        with open('profiles.txt', 'r') as file_record:
        lines = file_record.readlines()
        with open('profiles.txt', 'w') as file_writing:
            if line != str(n, a, p, l):
                file_writing.write(line)              
        return    
    
