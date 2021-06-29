# Aninfo-Módulo-Proyectos
Módulo Proyectos del sistema para la empresa PSA - Análisis de la Información FIUBA

# How to start:

### Requirements:
Python 3.6+

## How to install FastAPI:
```
pip install pipenv
```
```
sudo -H pipenv install fastapi uvicorn
```
```
pipenv shell
```

## How to run the server:

```
uvicorn app:app --reload
```

The command refers to:

**app**: the file app.py (the Python "module").

**app**: the object created inside of app.py with the line app = FastAPI().

**--reload**: make the server restart after code changes. Only use for development.

This opens on localhost and port 8000 --> http://127.0.0.1:8000