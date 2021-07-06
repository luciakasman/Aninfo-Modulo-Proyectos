from fastapi import FastAPI
from app.routers import task_controller, project_controller

app = FastAPI()

app.include_router(task_controller.router)
app.include_router(project_controller.router)

@app.get("/", tags=["Home"])
def home():
    return "Módulo Proyectos - by PSA"