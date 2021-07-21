from typing import Optional, List
from pydantic import BaseModel
from .resource import Resource
from enum import Enum
    
class TaskStatus(str,Enum):
    No_Iniciado = "No Iniciado"
    Iniciado = "Iniciado"
    Terminado = "Terminado"

class TaskRequest(BaseModel):
    name: str
    description: str
    associated_project_id: int
    assigned_worker: Resource
    fecha_inicio: str

class TaskWithoutId(TaskRequest):
    status: TaskStatus = TaskStatus.No_Iniciado
    fecha_fin: str = ""

class Task(TaskWithoutId):
    id: int
    