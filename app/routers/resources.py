from pydantic import BaseModel

class Resource(BaseModel):
    id: int
    name: str