Feature: Task

  Scenario: 1 - Consulto y no hay tareas existentes - get_all
    Given que no hay tareas existentes
    When consulto las tareas
    Then no me muestra ninguna tarea

  Scenario: 2- Como usuario, quiero poder obtener los datos de una tarea para consultar y comunicar su situación. - get_by_id
    Given que soy un usuario y quiero visualizar la información de una tarea
    When  solicito la información con el identificador de la tarea
    Then el sistema muestra la tarea con los datos: nombre, descripción, id del proyecto asociado, personas asignadas, fecha de inicio.

  Scenario: 3- Camino E: Como usuario, quiero poder agregar tareas al sistema para consultar y comunicar su situación. - create
    Given  que necesito crear tareas al sistema
    When  agrego una tarea
    Then  la misma con su correspondiente información se almacena en el sistema.

  Scenario: 4- Camino : Como usuario, quiero poder modificar tareas para actualizar la información. - update
    Given que necesito actualizar la información de una tarea
    When modifico la tarea
    Then el sistema guarda la tarea con los campos que le modifiqué, que pueden ser: el nombre, proyecto asociado, descripción, trabajador asignado.

  Scenario: 5- Como usuario, quiero poder borrar una tarea para evitar tener tareas en desuso.
      Given que quiero tener actualizadas las tareas
      When una tarea está en desuso y la elimino
      Then el sistema la borra y no muestra más su información



