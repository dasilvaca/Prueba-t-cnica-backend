# Prueba Técnica Backend

En el presente repositorio se encuentra la pruba técnica de Backend para la convocatoria.

Para hacer uso de la aplicación se requiere:
1. Instalar las dependencias usando el comando: `pip -r requirements.txt`

1. Ejecutar el comando `python manage.py migrate ecosystem`  y `python manage.py migrate`para crear las tablas de la base de datos.

1. Ejecutar la aplicación usando el comando: `python manage.py runserver`

1. Se deben crear Profesores, Cursos y Estudiantes con el fin de poder realizar una tarea perteneciente a un curso. Dicha tarea se podrá modificar, mostrar o borrar. La tarea como tal es creada por el profesor. El estudiante podrá subir la tarea correspondiente al curso, y el profesor tendrá dos endpoints adicionales para calificar la tarea y mostrar lo que el estudiante subió.

1. Se hace la invitación para ver las rutas de cada endpoint en el apartado de PruebaTécnicaBackend/urls.py.

1. Una vez ejecutado el servidor, se podrá accedar a cada una de las vistas y endpoints. El "body" de cada solicitud con el esqueleto del archivo JSON para el consumo de los servicios se encuentra en cada endpoint en el enlace de "raw data" provisto por Django REST framework