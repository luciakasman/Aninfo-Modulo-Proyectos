from fastapi import APIRouter
from .task import Task, TaskRequest, TaskWithoutId
from .project import Project
from .helper import Message
from fastapi.responses import JSONResponse
import random
from datetime import datetime
import json
from fastapi.encoders import jsonable_encoder
import os

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

@router.get("/", description= "Fetch all tasks")
async def get_all_tasks():
    return get_tasks()

@router.get("/{task_id}", description= "Fetch a single task by Id", response_model=Task, responses={404: {"model": Message}})
async def get_task_by_id(task_id: int):
    tasks = get_tasks()
    for task in tasks:
        if task["id"] == task_id:
            return task
    return JSONResponse(status_code=404, content={"message": "La tarea buscada no existe"})

@router.post("/", description= "Create a new task", responses= {404: {"model": Message}})
async def create_task(task_request: TaskRequest):
    try:
        random.seed(datetime.now())
        new_task = Task(**task_request.dict(), id = random.randrange(0, 10000))
        projects = read_json_file()
        if projects == []:
            return JSONResponse(status_code=404, content={"message": "No se pueden crear tareas si no existen proyectos."})
        for project in projects:
            if project["id"] == task_request.id_proyecto_asociado:
                project["tareas"].append(new_task)
                update_json_file(projects)
                return "todo ok!"
    except:
        return JSONResponse(status_code=404, content={"message": "Error al crear nueva tarea"})

@router.put("/{task_id}", description="Update task by Id", responses={404: {"model": Message}})
def update_task(task_id: int, new_task: TaskWithoutId):
    updated_task = Task(**new_task.dict(), id = task_id)
    projects = read_json_file()
    for project in projects:
        if project["id"] == updated_task.id_proyecto_asociado:
            for task in project["tareas"]:
                if task["id"] == task_id:
                    project["tareas"].remove(task)
                    project["tareas"].append(updated_task)
                    update_json_file(projects)
                    return "Se pudo actualizar la tarea correctamente"
    return JSONResponse(status_code=404, content={"message": "No existe la tarea que se desea actualizar"})

@router.delete("/{task_id}", description="Delete task by Id", responses={404: {"model": Message}})
def delete_task(task_id: int):
    projects = read_json_file()
    for project in projects:
        for task in project["tareas"]:
            if task["id"] == task_id:
                project["tareas"].remove(task)
                update_json_file(projects)
                return "Se pudo eliminar la tarea correctamente"
    return JSONResponse(status_code=404, content={"message": "No existe la tarea que se desea eliminar"})

def update_json_file(all_projects: list[Project]):
    with open("./projects.txt", "w") as projects_file:
        json.dump([jsonable_encoder(project) for project in all_projects], projects_file, indent=2, sort_keys=True)

def read_json_file():
    if os.stat("./projects.txt").st_size != 0:
        with open("./projects.txt", "r+") as projects_file:
            return json.load(projects_file)
    return []

def get_tasks():
    projects = read_json_file()
    return flatten([project["tareas"] for project in projects if project["tareas"] is not None])    # mejorar (if possible) para que no necesite el flatten

def flatten(t):
    return [item for sublist in t for item in sublist]