from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from project import Project
from fastapi.encoders import jsonable_encoder
from fastapi.responses import ORJSONResponse
import json

app = FastAPI()

projects = []

class Message(BaseModel):
    message: str

@app.get("/")
def home():
    return "Proyectos - by PSA"

@app.get('/projects',description="Fetch all projects")
async def get_all_projects():
    return sorted(projects, key=lambda x: x.id)

@app.get('/projects/{project_id}', description="Fetch a single project by Id", response_model=Project, responses={404: {"model": Message}})
async def get_project_by_id(project_id: int):
    for project in projects:
        if project.id == project_id:
            return project
    return JSONResponse(status_code=404, content={"message": "El proyecto buscado no existe"})

@app.post("/projects/", description="Create a new project", responses={404: {"model": Message}})
async def create_project(project: Project):
    try:
        projects.append(project)
#        with open('projects_db.json', 'a') as projects_db:
#            json.dump(jsonable_encoder(project), projects_db)
        return "todo ok!"
    except:
        return JSONResponse(status_code=404, content={"message": "Error al crear nuevo proyecto"})

@app.put("/project/{project_id}", description="Update project by Id", responses={404: {"model": Message}})
def update_project(project_id: int, new_project: Project):
    for project in projects:
        if project.id == project_id:
            projects.remove(project)
            projects.append(new_project)
            return "Se pudo actualizar el proyecto correctamente"
    return JSONResponse(status_code=404, content={"message": "No existe el proyecto que se desea actualizar"})

@app.delete("/project/{project_id}", description="Delete project by Id", responses={404: {"model": Message}})
def delete_project(project_id: int):
    for project in projects:
        if project.id == project_id:
            projects.remove(project)
            return "Se pudo eliminar el proyecto correctamente"
    return JSONResponse(status_code=404, content={"message": "No existe el proyecto que se desea eliminar"})