from fastapi import APIRouter
from .task import Task, TaskRequest, TaskWithoutId
from .helper import Message
from fastapi.responses import JSONResponse
import random
from datetime import datetime

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

tasks = []

@router.get("/", description= "Fetch all tasks")
async def get_all_tasks():
    return sorted(tasks, key = lambda x: x.id)

@router.get("/{task_id}", description= "Fetch a single task by Id", response_model=Task, responses={404: {"model": Message}})
async def get_task_by_id(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    return JSONResponse(status_code=404, content={"message": "La tarea buscada no existe"})

@router.post("/", description= "Create a new task", responses= {404: {"model": Message}})
async def create_task(task_request: TaskRequest):
    try:
        id = random.randrange(0, 10000)
        random.seed(datetime.now())
        tasks.append(Task(**task_request.dict(), id = id))
        return id
    except:
        return JSONResponse(status_code=404, content={"message": "Error al crear nueva tarea"})

@router.put("/{task_id}", description="Update task by Id", responses={404: {"model": Message}})
def update_task(task_id: int, new_task: TaskWithoutId):
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            tasks.append(Task(**new_task.dict(), id = task_id))
            return "Se pudo actualizar la tarea correctamente"
    return JSONResponse(status_code=404, content={"message": "No existe la tarea que se desea actualizar"})

@router.delete("/{task_id}", description="Delete task by Id", responses={404: {"model": Message}})
def delete_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            return "Se pudo eliminar la tarea correctamente"
    return JSONResponse(status_code=404, content={"message": "No existe la tarea que se desea eliminar"})