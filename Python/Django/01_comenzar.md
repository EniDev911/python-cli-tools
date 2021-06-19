## Comenzar un proyecto con Django  

Asumiendo que ya tenemos la librería instalada, ya sea en virtual o en local, podemos crear un proyecto con el siguiente comando utilizando el script habilitado por django.  

    django-admin startproject Project_name

Una vez se crea el proyecto lo siguiente es entrar en la carpeta y utilizando el scrip **manage.py** es crear las tablas de la base de datos, ya que son necesaria para la interfaz administrativa de Django. Por defecto ya viene configurado el gestor Sqlite3, no hay que mover nada solo ejecutando el siguiente comando.  

    python manage.py migrate

**Comprobar el funcionamiento**  

Ya hecha la migración, podemos correr el servidor que trae Django por defecto para las pruebas.  

    python manage.py runserver


## Crear una primera petición y responder con un mensaje  

Para eso Django trabaja con objetos de tipo **Request** y **HttpResponse**, dentro del proyecto creamos un archivo llamado **views.py**  

