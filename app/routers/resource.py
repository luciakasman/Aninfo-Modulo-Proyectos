from pydantic import BaseModel

class Resource(BaseModel):
    legajo: int
    nombre: str
    apellido: str