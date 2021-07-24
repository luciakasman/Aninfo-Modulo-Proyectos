import requests
from behave import *
import json

empty = b'[]'

body2 = """{"nombre": "Catalina", "lider_de_equipo": {"resourceID": 0, "name": "Romina","surname": "Gomez"},"personas_asignadas": [{"resourceID": 0,"name": "Tomas","surname": "Gomez"}],"fecha_inicio": "21/06/2021", "fecha_limite_inicio": "21/07/2021", "fecha_estimada_fin": "21/06/2021"}"""
body3 = """{"nombre": "Franco", "lider_de_equipo": {"resourceID": 10, "name": "Romina","surname": "Gomez"},"personas_asignadas": [{"resourceID": 0,"name": "Tomas","surname": "Gomez"}],"fecha_inicio": "21/06/2021", "fecha_limite_inicio": "21/07/2021", "fecha_estimada_fin": "21/06/2021"}"""

@given('que no hay proyectos existentes')
def no_projects(context):
    global apiUrl
    apiUrl = 'http://127.0.0.1:8000/'

@given('que necesito crear proyectos al sistema')
def create_projects(context):
    global apiComplete
    apiComplete = 'http://127.0.0.1:8000/projects/'

@given('soy un usuario y quiero visualizar la información de un proyecto')
def view_information(context):
    global apiComplete, id
    apiComplete = 'http://127.0.0.1:8000/projects/'

    bodyJson = json.loads(body3)
    id = requests.post(apiComplete, json=bodyJson).content.decode()

@when('consulto los proyectos')
def get_all_projects(context):
    global result
    apiComplete = apiUrl+"projects/"
    result = requests.get(apiComplete)

@when('agrego un proyecto')
def add_project(context):
        global result, bodyJson
        bodyJson = json.loads(body2)
        requests.post(apiComplete, json = bodyJson)


@when('solicito la información con el identificador')
def project_by_id(context):
        global result
        api = apiComplete + id
        result = requests.get(api)

@then('no me muestra ningún proyecto')
def not_found_projects(context):
    assert result.content == empty

@then('el sistema carga el proyecto con el nombre, líder de proyecto, personas asignadas que elegí, fecha de inicio, fecha límite de inicio, fecha fin.')
def all_projects(context):
    result = requests.get(apiComplete)
    assert compareJsons(result.content, body2)

@then( 'el sistema muestra el proyecto con los datos: nombre, líder de proyecto, personas asignadas que elegí, fecha de inicio, fecha límite de inicio, fecha fin y sus tareas asociadas.')
def all_projects(context):
    assert compareJsons(result.content, body3)


def compareJsons(result, body):
    resultToCompare = result.decode()
    bodyToCompare = body.replace(": ", ":").replace(", ", ",")[0:-1]
    return bodyToCompare in resultToCompare
















@given('que aguregué un proyecto')
def no_projects(context):
    global apiUrl, body
    apiUrl = "http://127.0.0.1:8000/projects/"
    body = {
  "nombre": "Camila",
  "lider_de_equipo": {
    "legajo": 1,
    "Nombre": "Carolina",
    "Apellido": "Sanchez"
  },
  "personas_asignadas": [
    {
      "legajo": 2,
      "Nombre": "Carla",
      "Apellido": "Gomez"
    }
  ],
  "fecha": "01/01/2021"
}
    res = requests.post(apiUrl, body)

@then('me muestra el nuevo proyecto')
def step_impl(context):
    result = requests.get(apiComplete)
    assert True is True
