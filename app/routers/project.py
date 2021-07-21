from typing import Optional, List
from pydantic import BaseModel
from .resource import Resource
from enum import Enum
    
class ProjectStatus(str, Enum):
    No_iniciado = "No Iniciado"
    Iniciado = "Iniciado"
    Terminado = "Terminado"

class ProjectRequest(BaseModel):
    nombre: str
    lider_de_equipo: Resource
    personas_asignadas: List[Resource] #despues va a tener que ser una lista de empleados. Lo mismo con Tareas (TODO)
    fecha_inicio: str
    fecha_limite_inicio: str
    fecha_estimada_fin: str

class Project(ProjectRequest):
    id: int
    estado: ProjectStatus = ProjectStatus.No_iniciado
    porcentaje_de_avance: float = 0.0
    fecha_fin: str = ""

    class Config:  
        use_enum_values = True

