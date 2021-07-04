from typing import Optional, List
from pydantic import BaseModel
from enum import Enum

class TaskStatus(str,Enum):
    No_Iniciado = "No Iniciado"
    Iniciado = "Iniciado"
    Terminado = "Terminado"

class TaskRequest(BaseModel):
    id: int
    name: int
    description: str
    associated_project_id: int
    assigned_worker: int

class Task(TaskRequest):
    status: TaskStatus = TaskStatus.No_Iniciado
    