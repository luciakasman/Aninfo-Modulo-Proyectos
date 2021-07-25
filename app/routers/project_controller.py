from fastapi import APIRouter
from .project import Project, ProjectStatus, ProjectRequest, ProjectWithoutId
from .helper import Message
from fastapi.responses import JSONResponse
import random
from datetime import datetime
import json
from fastapi.encoders import jsonable_encoder
import os

router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)

@router.get('/',description="Fetch all projects")
async def get_all_projects():
    return read_json_file()

@router.get('/{project_id}', description="Fetch a single project by Id", response_model=Project, responses={404: {"model": Message}})
async def get_project_by_id(project_id: int):
    all_projects = read_json_file()
    for project in all_projects:
        if project["id"] == project_id:
            return project
    return JSONResponse(status_code=404, content={"message": "El proyecto buscado no existe"})

@router.post("/", description="Create a new project", responses={404: {"model": Message}})
async def create_project(project_request: ProjectRequest):
    try:
        id = random.randrange(0, 10000)
        random.seed(datetime.now())
        create_json_file(Project(**project_request.dict(), id = id))
        return id
    except:
        return JSONResponse(status_code=404, content={"message": "Error al crear nuevo proyecto"})

@router.put("/{project_id}", description="Update project by Id", responses={404: {"model": Message}})
def update_project(project_id: int, new_project: ProjectWithoutId):
    all_projects = read_json_file()
    for project in all_projects:
        if project["id"] == project_id:
            all_projects.remove(project)
            all_projects.append(Project(**new_project.dict(), id = project_id))
            update_json_file(all_projects)
            return "Se pudo actualizar el proyecto correctamente"      
    return JSONResponse(status_code=404, content={"message": "No existe el proyecto que se desea actualizar"})

@router.delete("/{project_id}", description="Delete project by Id", responses={404: {"model": Message}})
def delete_project(project_id: int):
    all_projects = read_json_file()
    for project in all_projects:
        if project["id"] == project_id:
            all_projects.remove(project)
            update_json_file(all_projects)
            return "Se pudo eliminar el proyecto correctamente"
    return JSONResponse(status_code=404, content={"message": "No existe el proyecto que se desea eliminar"})

def update_json_file(all_projects: list[Project]):
    with open("./projects.txt", "w") as projects_file:
        json.dump([jsonable_encoder(project) for project in all_projects], projects_file, indent=2, sort_keys=True)

def create_json_file(project: Project):
    data = read_json_file()
    data.append(jsonable_encoder(project))
    with open("./projects.txt", "w") as projects_file:
        json.dump(data, projects_file, indent=2, sort_keys=True)

def read_json_file():
    if os.stat("./projects.txt").st_size != 0:
        with open("./projects.txt", "r+") as projects_file:
            return json.load(projects_file)
    return []