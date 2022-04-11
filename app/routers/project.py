from typing import Optional, List
from pydantic import BaseModel
from typing import Optional
from .resource import Resource
from .task import Task
from enum import Enum
    
class ProjectStatus(str, Enum):
    No_iniciado = "No Iniciado"
    Iniciado = "Iniciado"
    Terminado = "Terminado"

class ProjectRequest(BaseModel):
    nombre: str
    descripcion: str
    lider_de_equipo: Resource
    personas_asignadas: List[Resource]
    fecha_inicio: str
    fecha_limite_inicio: str
    fecha_estimada_fin: str

class ProjectWithoutId(ProjectRequest):
    estado: ProjectStatus = ProjectStatus.No_iniciado
    porcentaje_de_avance: float = 0.0
    fecha_fin: str = ""
    
    class Config:
        use_enum_values = True

class Project(ProjectWithoutId):
    id: int
    tareas: Optional[List[Task]] = []