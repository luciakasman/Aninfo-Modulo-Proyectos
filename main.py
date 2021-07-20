from fastapi import FastAPI
from app.routers import task_controller, project_controller
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(task_controller.router)
app.include_router(project_controller.router)

@app.get("/", tags=["Home"])
def home():
    return "Módulo Proyectos - by PSA"