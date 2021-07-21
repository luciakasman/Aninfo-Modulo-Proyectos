from typing import Optional, List
from pydantic import BaseModel
from .resource import Resource
from enum import Enum
    
class TaskStatus(str,Enum):
    No_Iniciado = "No Iniciado"
    Iniciado = "Iniciado"
    Terminado = "Terminado"

class TaskRequest(BaseModel):
    nombre: str
    descripcion: str
    id_proyecto_asociado: int
    persona_asignada: Resource
    fecha_inicio: str

class TaskWithoutId(TaskRequest):
    estado: TaskStatus = TaskStatus.No_Iniciado
    fecha_fin: str = ""

class Task(TaskWithoutId):
    id: int
    