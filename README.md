# Aninfo-Módulo-Proyectos
Módulo Proyectos del sistema para la empresa PSA - Análisis de la Información FIUBA

# Cómo comenzar:

### Requerimientos:
Python 3.6+

## Cómo instalar FastAPI:
Instalar el entorno virtual pipenv *[opcional]*:
```
pip install pipenv
```
Instalar FastAPI y uvicorn (necesario para manejar dependencias):
```
sudo -H pipenv install fastapi uvicorn
```
Activar el entorno virtual *[opcional]*:
```
pipenv shell
```

## Cómo levantar el servidor:

```
uvicorn main:app --reload
```

El comando refiere a:

**app**: el archivo app.py (el "módulo" de Python).

**app**: el objeto creado adentro de app.py con la línea app = FastAPI().

**--reload**: hace que el servidor se reinice después de un cambio en el código. Sólo se usa para desarrollo.

Esto levanta en localhost en el puerto 8000 --> http://127.0.0.1:8000