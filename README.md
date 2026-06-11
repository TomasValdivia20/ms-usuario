ReadMe MicroServicio Usuario:

En este readme encontraran todo lo relacionado con el microservicio de usuario:
encontraran multiples funciones tales como crear,eliminar,editar,actualizar
la cual tienen interaccion con el usuario.

Este microservicio esta hecho con Django, el cual utiliza Python, por lo cual
debemos seguir los siguientes pasos para poder correr este microservicio


Crear entorno virtual:
python -m venv venv

En Windows: venv\Scripts\activate
Instalar dependencias:

pip install -r requirements.txt

Migraciones:

python manage.py migrate

Crear Superusuario (opcional para el admin de Django):

python manage.py createsuperuser

luego deben poner un correo y contraseña que se acuerden

luego de eso deben correr el servidor

python manage.py runserver

tambien para ver el Swager a la url que le entreguen deran colocarle al lado de eso lo siguiente

/docs