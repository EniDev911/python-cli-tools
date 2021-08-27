
```bash
sudo apt install mysql-server
```
Este comando instala MySQL, pero ahora debemos configurarlo para usarlo de manera más 

## Configuración: MySQL

Para cuando instalamos MySQL nos da una secuencia de comandos incluida en DBMS. Esta secuencia cambia algunas de las opciones predeterminadas menos seguras para cosas como inicios de sesión root remotos y usuarios de ejemplos.  

Ejecutamos el script de seguridad con sudo:

```bash
sudo mysql_secure_installation
```

La primera pregunta nos solicitará si queremos validar que nuestro password para conectarnos al servidor sea seguro, si lo deseamos al momento de crear nuestro password MySQL nos validará si cumple con las condiciones mínimas de seguridad. Si no queremos esto solamente ingresamos N

```
Securing the MySQL server deployment.

Connecting to MySQL using a blank password.

VALIDATE PASSWORD COMPONENT can be used to test passwords
and improve security. It checks the strength of password
and allows the users to set only those passwords which are
secure enough. Would you like to setup VALIDATE PASSWORD component?

Press y|Y for Yes, any other key for No: Y
```

Luego de acuerdo a la opción que ingresemos nos solicitará ingresar el password para el usuario root:

```bash
New password: 

Re-enter new password: 
```

Una vez ingresamos nuestro password, nos preguntará si deseamos remover a los usuarios ánonimos que se crean por defecto junto a la instalación de MySQL, lo mejor es removerlos.  

```bash
By default, a MySQL installation has an anonymous user,
allowing anyone to log into MySQL without having to have
a user account created for them. This is intended only for
testing, and to make the installation go a bit smoother.
You should remove them before moving into a production
environment.

Remove anonymous users? (Press y|Y for Yes, any other key for No) : Y
```

Normalmente, a root solo se le debe permitir conectarse desde 'localhost'. Para así asegurar que no puedan adivinar la password de root desde la red. Así que deshabilitamos el logín remoto.  

```bash
Normally, root should only be allowed to connect from
'localhost'. This ensures that someone cannot guess at
the root password from the network.

Disallow root login remotely? (Press y|Y for Yes, any other key for No) : Y 
```

Luego nos preguntá si queremos eliminar la base de datos de prueba, esto es opcional. 

```bash
Remove test database and access to it? (Press y|Y for Yes, any other key for No) : Y
```
Luego nos pregunta si queremos recargar la tabla de privilegios. Pondremos si (Y).  

```bash
Reload privilege tables now? (Press y|Y for Yes, any other key for No) : y
```







