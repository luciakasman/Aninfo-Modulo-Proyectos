Feature: Project

  Scenario: 1- Camino Inicial: Consulto los proyectos - get_all
    Given soy un usuario y quiero visualizar los proyectos existentes
    When consulto los proyectos
    Then el sistema muestra los proyectos con los datos: nombre, líder de proyecto, personas asignadas que elegí, fecha de inicio, fecha límite de inicio, fecha fin y sus tareas asociadas.

 Scenario: 2- Camino A: Como usuario, quiero poder agregar proyectos para consultar y comunicar su situación. - create
    Given que necesito crear proyectos al sistema
    When agrego un proyecto
    Then el sistema carga el proyecto con el nombre, líder de proyecto, personas asignadas que elegí, fecha de inicio, fecha límite de inicio, fecha fin.

Scenario: 3- Camino : Como usuario, quiero poder obtener los datos de un proyectos para consultar y comunicar su situación. - get_by_id
  Given  soy un usuario y quiero visualizar la información de un proyecto
  When  solicito la información con el identificador
  Then el sistema muestra el proyecto con los datos: nombre, líder de proyecto, personas asignadas que elegí, fecha de inicio, fecha límite de inicio, fecha fin y sus tareas asociadas.

Scenario: 4- Camino B: Como usuario, quiero poder modificar proyectos para actualizar la información. - update
  Given que necesito actualizar la información de un proyecto existente
  When modifico el proyecto
  Then el sistema guarda el proyecto con los campos que le modifiqué, que pueden ser: el nombre, líder de proyecto, personas asignadas, fecha de inicio, fecha límite de inicio, fecha fin y/o tareas vinculadas al proyecto.

Scenario: Como usuario, quiero poder borrar un proyecto para evitar tener proyectos en desuso.
    Given que quiero tener actualizados los proyectos
    When un proyecto está en desuso y lo elimino
    Then el sistema lo borra y no muestra más su información
