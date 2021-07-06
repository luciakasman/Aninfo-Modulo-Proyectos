#Asi propongo que se hagan los controladores por separado.

from fastapi import APIRouter
from .task import Task, TaskRequest, Message
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

task_router = APIRouter()

tasks = []

@task_router.get("/tasks", description= "Fetch all tasks")
async def get_all_tasks():
    return sorted(tasks, key = lambda x: x.id)

@task_router.get("/tasks/{task_id}", description= "Fetch a single task by Id", response_model=Task, responses={404: {"model": Message}})
async def get_task_by_id(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    return JSONResponse(status_code=404, content={"message": "La tarea buscada no existe"})

@task_router.post("/tasks/", description= "Create a new task", responses= {404: {"model": Message}})
async def create_task(task_request: TaskRequest):
    try:
        tasks.append(create_new_task(task_request))
        return "todo liso"
    except:
        return JSONResponse(status_code=404, content={"message": "Error al crear nueva tarea"})

#esto deberia ir en el Service  
def create_new_task(task_request: TaskRequest):
    new_task = Task(**task_request.dict())
    return new_task

@task_router.put("/tasks/{task_id}", description="Update task by Id", responses={404: {"model": Message}})
def update_project(task_id: int, new_task: TaskRequest):
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            tasks.append(create_new_task(new_task))
            return "Se pudo actualizar la tarea correctamente"
    return JSONResponse(status_code=404, content={"message": "No existe la tarea que se desea actualizar"})

@task_router.delete("/tasks/{task_id}", description="Delete task by Id", responses={404: {"model": Message}})
def delete_project(task_id: int):
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            return "Se pudo eliminar la tarea correctamente"
    return JSONResponse(status_code=404, content={"message": "No existe la tarea que se desea eliminar"})
