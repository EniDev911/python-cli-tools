
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

## Ajustar la autenticación y los privilegios de usuario (opcional):  

En los sistemas Ubuntu con MySQL 5.7 (y versiones posteriores), el usuario **root** de MySQL se configura para la autenticación usando el complemento **auth_socket** de manera predeterminada en lugar de una contraseña. Esto en muchos casos proporciona mayor seguridad y utilidad, pero también puede generar complicaciones cuando deba permitir que un programa externo (como phpMyAdmin) acceda al usuario.  

Para usar un password para conectar a MySQL como **root**, deberemos cambiar el método de autenticación de **auth_socket** a otro complemento, como **caching_sha2_password** o **mysql_native_password**. Para hacer esto, abra la consola de MySQL desde su terminal:

```bash
sudo mysql
```

Para ver el método de autenticación utilizado por las cuentas de usuarios de MySQL ejecutamos la siguiente sentencia dentro de la consola de MySQL:  

```bash
SELECT user, authentication_string, plugin, host FROM mysql.user;

Output
+------------------+------------------------------------------------------------------------+-----------------------+-----------+
| user             | authentication_string                                                  | plugin                | host      |
+------------------+------------------------------------------------------------------------+-----------------------+-----------+
| debian-sys-maint | $A$005$lS|M#3K #XslZ.xXUq.crEqTjMvhgOIX7B/zki5DeLA3JB9nh0KwENtwQ4 | caching_sha2_password | localhost |
| mysql.infoschema | $A$005$THISISACOMBINATIONOFINVALIDSALTANDPASSWORDTHATMUSTNEVERBRBEUSED | caching_sha2_password | localhost |
| mysql.session    | $A$005$THISISACOMBINATIONOFINVALIDSALTANDPASSWORDTHATMUSTNEVERBRBEUSED | caching_sha2_password | localhost |
| mysql.sys        | $A$005$THISISACOMBINATIONOFINVALIDSALTANDPASSWORDTHATMUSTNEVERBRBEUSED | caching_sha2_password | localhost |
| root             |                                                                        | auth_socket           | localhost |
+------------------+------------------------------------------------------------------------+-----------------------+-----------+
5 rows in set (0.00 sec)
```

Para configurar la cuenta **root** para autenticar con una password, ejecute una instrucción **ALTER USER** para cambiar qué complemento de autenticación utiliza y establecer una nueva password.  

Cambiamos por un password seguro,la siguiente instrucción cambiará el password de **root**:  

```bash
# Shell de mysql
ALTER USER 'root'@'localhost' IDENTIFIED WITH caching_sha2_password BY 'password';
```

Luego, ejecutamos la instrucción:  

```bash
# Shell de mysql
FLUSH PRIVILEGES;
```
Para indicar al servidor que vuelva a cargar la tabla de permisos y aplique los nuevos cambios.  






