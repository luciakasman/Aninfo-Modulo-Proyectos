from pydantic import BaseModel

class Resource(BaseModel):
    legajo: int
    Nombre: str
    Apellido: str