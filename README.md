# Aninfo-Modulo-Proyectos
Módulo Proyectos del sistema para la empresa PSA - Análisis de la Información FIUBA


## How to run the server:

```
uvicorn app:app --reload
```

The command refers to:

**app**: the file app.py (the Python "module").

**app**: the object created inside of app.py with the line app = FastAPI().

**--reload**: make the server restart after code changes. Only use for development.