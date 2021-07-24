import requests
from behave import *
import json

empty = b'[]'

body2 = """{"nombre": "Catalina", "lider_de_equipo": {"resourceID": 0, "name": "Romina","surname": "Gomez"},"personas_asignadas": [{"resourceID": 0,"name": "Tomas","surname": "Gomez"}],"fecha_inicio": "21/06/2021", "fecha_limite_inicio": "21/07/2021", "fecha_estimada_fin": "21/06/2021"}"""
body3 = """{"nombre": "Franco", "lider_de_equipo": {"resourceID": 10, "name": "Romina","surname": "Gomez"},"personas_asignadas": [{"resourceID": 0,"name": "Tomas","surname": "Gomez"}],"fecha_inicio": "21/06/2021", "fecha_limite_inicio": "21/07/2021", "fecha_estimada_fin": "21/06/2021"}"""
body4 = """{"nombre": "Tomas", "lider_de_equipo": {"resourceID": 10, "name": "Romina","surname": "Gomez"},"personas_asignadas": [{"resourceID": 0,"name": "Tomas","surname": "Gomez"}],"fecha_inicio": "21/06/2021", "fecha_limite_inicio": "21/07/2021", "fecha_estimada_fin": "21/06/2021"}"""
body4Edited = """{"nombre": "Lautaro", "lider_de_equipo": {"resourceID": 10, "name": "Romina","surname": "Gomez"},"personas_asignadas": [{"resourceID": 0,"name": "Tomas","surname": "Gomez"}],"fecha_inicio": "21/06/2021", "fecha_limite_inicio": "21/07/2021", "fecha_estimada_fin": "21/06/2021"}"""
body5 = """{"nombre": "Julieta", "lider_de_equipo": {"resourceID": 10, "name": "Romina","surname": "Gomez"},"personas_asignadas": [{"resourceID": 0,"name": "Tomas","surname": "Gomez"}],"fecha_inicio": "21/06/2021", "fecha_limite_inicio": "21/07/2021", "fecha_estimada_fin": "21/06/2021"}"""
completeApi = 'http://127.0.0.1:8000/projects/'


@given('que no hay proyectos existentes')
def no_projects(context):
    global apiUrl
    apiUrl = 'http://127.0.0.1:8000/'

@given('que necesito crear proyectos al sistema')
def create_projects(context):
    global completeApi
    completeApi = 'http://127.0.0.1:8000/projects/'

@given('soy un usuario y quiero visualizar la información de un proyecto')
def view_information(context):
    global id

    bodyJson = json.loads(body3)
    id = requests.post(completeApi, json=bodyJson).content.decode()


@given('que necesito actualizar la información de un proyecto existente')
def update_information(context):
    global id

    bodyJson = json.loads(body4)
    id = requests.post(completeApi, json=bodyJson).content.decode()

@given('que quiero tener actualizados los proyectos')
def update_information(context):
    global id

    bodyJson = json.loads(body5)
    id = requests.post(completeApi, json=bodyJson).content.decode()


@when('consulto los proyectos')
def get_all_projects(context):
    global result
    completeApi = apiUrl+"projects/"
    result = requests.get(completeApi)

@when('agrego un proyecto')
def add_project(context):
        global result, bodyJson
        bodyJson = json.loads(body2)
        requests.post(completeApi, json = bodyJson)


@when('solicito la información con el identificador')
def project_by_id(context):
        global result
        api = completeApi + id
        result = requests.get(api)

@when('modifico el proyecto')
def modify_project(context):
        global result, url
        url = completeApi + id
        bodyJson = json.loads(body4Edited)

        result = requests.put(url, json = bodyJson)

@when('un proyecto está en desuso y lo elimino')
def modify_project(context):
        global result, url
        url = completeApi + id

        result = requests.delete(url)

@then('no me muestra ningún proyecto')
def not_found_projects(context):
    assert result.content == empty

@then('el sistema carga el proyecto con el nombre, líder de proyecto, personas asignadas que elegí, fecha de inicio, fecha límite de inicio, fecha fin.')
def all_projects(context):
    result = requests.get(completeApi)
    assert compareJsons(result.content, body2)

@then( 'el sistema muestra el proyecto con los datos: nombre, líder de proyecto, personas asignadas que elegí, fecha de inicio, fecha límite de inicio, fecha fin y sus tareas asociadas.')
def all_projects(context):
    assert compareJsons(result.content, body3)

@then( 'el sistema guarda el proyecto con los campos que le modifiqué, que pueden ser: el nombre, líder de proyecto, personas asignadas, fecha de inicio, fecha límite de inicio, fecha fin y/o tareas vinculadas al proyecto.')
def all_projects(context):
    result = requests.get(url)
    assert compareJsons(result.content, body4Edited)
    assert not compareJsons(result.content, body4)

@then( 'el sistema lo borra y no muestra más su información')
def all_projects(context):
    result = requests.get(url)
    assert not compareJsons(result.content, body5)

def compareJsons(result, body):
    resultToCompare = result.decode()
    bodyToCompare = body.replace(": ", ":").replace(", ", ",")[0:-1]
    return bodyToCompare in resultToCompare

