## ¿Cuál es el propósito del usuario "mysql.sys@localhost"?

El usuario **mysql.sys@localhost** es un usuario del sistema que se utiliza como definidor de vistas, procedimientos y funciones en el esquema sys. Se agrego en MySQL 5.7.9 para evitar problemas si el DBA cambia el nombre del usuario 'root'@'localhost':  

Lo siguiente se aplica al usuario mysql.sys@localhost  


1. Es un usuario obligatorio siempre que esté instalado el esquema sys.  

2. Está bloqueado de forma predeterminada, por lo que no se puede utilizar para acceder a MySQL.
