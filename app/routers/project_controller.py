from fastapi import APIRouter
from .project import Project, ProjectStatus, ProjectRequest
from .helper import Message
from fastapi.responses import JSONResponse
import random
from datetime import datetime

router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)

projects = []

@router.get('/',description="Fetch all projects")
async def get_all_projects():
    return sorted(projects, key=lambda x: x.id)

@router.get('/{project_id}', description="Fetch a single project by Id", response_model=Project, responses={404: {"model": Message}})
async def get_project_by_id(project_id: int):
    for project in projects:
        if project.id == project_id:
            return project
    return JSONResponse(status_code=404, content={"message": "El proyecto buscado no existe"})

@router.post("/", description="Create a new project", responses={404: {"model": Message}})
async def create_project(project_request: ProjectRequest):
    try:
        random.seed(datetime.now())
        projects.append(Project(**project_request.dict(), id = random.randrange(0, 10000)))
        return "todo ok!"
    except:
        return JSONResponse(status_code=404, content={"message": "Error al crear nuevo proyecto"})

@router.put("/{project_id}", description="Update project by Id", responses={404: {"model": Message}})
def update_project(project_id: int, new_project: Project):
    for project in projects:
        if project.id == project_id:
            projects.remove(project)
            projects.append(Project(**new_project.dict(), id = project_id))
            return "Se pudo actualizar el proyecto correctamente"
    return JSONResponse(status_code=404, content={"message": "No existe el proyecto que se desea actualizar"})

@router.delete("/{project_id}", description="Delete project by Id", responses={404: {"model": Message}})
def delete_project(project_id: int):
    for project in projects:
        if project.id == project_id:
            projects.remove(project)
            return "Se pudo eliminar el proyecto correctamente"
    return JSONResponse(status_code=404, content={"message": "No existe el proyecto que se desea eliminar"})