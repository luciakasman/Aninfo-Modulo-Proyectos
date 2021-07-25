import requests
from behave import *
import json

empty = b'[]'
completeApi = 'http://127.0.0.1:8000/tasks/'

body2 = """{"nombre": "Florencia","descripcion": "string", "id_proyecto_asociado": 0,"persona_asignada": {"resourceID": 0,"name": "string","surname": "string"},"fecha_inicio": "string"}"""
body3 = """{"nombre": "Santiago","descripcion": "string", "id_proyecto_asociado": 0,"persona_asignada": {"resourceID": 0,"name": "string","surname": "string"},"fecha_inicio": "string"}"""
body4 = """{"nombre": "Lucas","descripcion": "string", "id_proyecto_asociado": 0,"persona_asignada": {"resourceID": 0,"name": "string","surname": "string"},"fecha_inicio": "string"}"""
body4Edited = """{"nombre": "Agustina","descripcion": "string", "id_proyecto_asociado": 0,"persona_asignada": {"resourceID": 0,"name": "string","surname": "string"},"fecha_inicio": "string"}"""
body5 = """{"nombre": "Martin","descripcion": "string", "id_proyecto_asociado": 0,"persona_asignada": {"resourceID": 0,"name": "string","surname": "string"},"fecha_inicio": "string"}"""

@given('que no hay tareas existentes')
def no_tasks(context):
    global apiUrl
    apiUrl = 'http://127.0.0.1:8000/'

@given('que soy un usuario y quiero visualizar la información de una tarea')
def view_information(context):
    global id
    bodyJson = json.loads(body2)
    id = requests.post(completeApi, json=bodyJson).content.decode()

@given('que necesito crear tareas al sistema')
def create_tasks(context):
    global completeApi
    completeApi = 'http://127.0.0.1:8000/tasks/'

@given('que necesito actualizar la información de una tarea')
def update_information(context):
    global id
    bodyJson = json.loads(body4)
    id = requests.post(completeApi, json=bodyJson).content.decode()

@given('que quiero tener actualizadas las tareas')
def update_tasks(context):
    global id
    bodyJson = json.loads(body5)
    id = requests.post(completeApi, json=bodyJson).content.decode()


@when('consulto las tareas')
def get_all_tasks(context):
    global result
    completeApi = apiUrl+"tasks/"
    result = requests.get(completeApi)

@when('solicito la información con el identificador de la tarea')
def task_by_id(context):
        global result
        api = completeApi + id
        result = requests.get(api)

@when('agrego una tarea')
def add_task(context):
        global result, bodyJson
        bodyJson = json.loads(body3)
        requests.post(completeApi, json = bodyJson)

@when('modifico la tarea')
def modify_task(context):
        global result, url
        url = completeApi + id
        bodyJson = json.loads(body4Edited)

        result = requests.put(url, json = bodyJson)

@when('una tarea está en desuso y la elimino')
def delete_task(context):
        global result, url
        url = completeApi + id
        result = requests.delete(url)


@then('no me muestra ninguna tarea')
def not_found_tasks(context):
    assert result.content == empty

@then('el sistema muestra la tarea con los datos: nombre, descripción, id del proyecto asociado, personas asignadas, fecha de inicio.')
def all_information(context):
    assert compareJsons(result.content, body2)

@then( 'la misma con su correspondiente información se almacena en el sistema.')
def task_information(context):
    result = requests.get(completeApi)
    assert compareJsons(result.content, body3)

@then( 'el sistema guarda la tarea con los campos que le modifiqué, que pueden ser: el nombre, proyecto asociado, descripción, trabajador asignado.')
def save_task(context):
    result = requests.get(url)
    assert compareJsons(result.content, body4Edited)
    assert not compareJsons(result.content, body4)

@then( 'el sistema la borra y no muestra más su información')
def delete_task(context):
    result = requests.get(url)
    assert not compareJsons(result.content, body5)


def compareJsons(result, body):
    resultToCompare = result.decode()
    bodyToCompare = body.replace(": ", ":").replace(", ", ",")[0:-1]
    return bodyToCompare in resultToCompare

