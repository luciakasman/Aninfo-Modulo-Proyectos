from typing import Optional
from pydantic import BaseModel
from enum import Enum

class ProjectStatus(str, Enum):
    No_iniciado = "No Iniciado"
    Iniciado = "Iniciado"
    Terminado = "Terminado"

class Project(BaseModel):
    id: int
    nombre: str
    estado: Optional[ProjectStatus] = ProjectStatus.No_iniciado
    porcentaje_de_avance: Optional[float] = 0
    lider_de_equipo: str
    personas_asignadas: list

    class Config:  
        use_enum_values = True