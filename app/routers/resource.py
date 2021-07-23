from pydantic import BaseModel

class Resource(BaseModel):
    resourceID: int
    name: str
    surname: str
