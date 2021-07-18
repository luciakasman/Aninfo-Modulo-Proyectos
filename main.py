from fastapi import FastAPI
from app.routers import task_controller, project_controller
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:5000",
]

middleware = [
    Middleware(CORSMiddleware, allow_origins=origins)
]

app = FastAPI(middleware=middleware)

app.include_router(task_controller.router)
app.include_router(project_controller.router)

@app.get("/", tags=["Home"])
def home():
    return "Módulo Proyectos - by PSA"