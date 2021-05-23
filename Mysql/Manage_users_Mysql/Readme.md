<h2 align="center">Administrar usuarios en mysql.</h2>

Para crear cuentas de usuario en <b>mysql</b> se necesita tener permisos de usuarios. Por medio del comando <strong>CREATE USER</strong>. A cada cuenta se le puede asignar una contraseña por medio de la cláusula <strong>IDENTIFIED BY</strong>, si desea que la contraseña se guarde en texto plano, no se utilizará la palabra <strong>Password</strong> caso contrario la contraseña se guardará cifrada con el valor hash que es devuelto por la función <strong>Password()</strong>   

<b>Ejemplo:</b>  

```sql
mysql>CREATE USER 'user'@'server' IDENTIFIED BY 'passworduser';
```

<p align="center">
    <img src="img/01_create_user.png" width="500" height="350">
</p>

El usaurio ha sido creado, sin embargo puede conectarse al servidor pero hace falta asignarle los diferentes privilegios, para que pueda realizar cualquier tipo de tarea.  

<h2 align="center">Privilegios de usuarios</h2>  

Para ver los privilegios asignados a una cuenta utilizamos la sentencia <b>SHOW GRANTS</b> para el usuario conectado. Para consultar los privilegios que tiene otro usuario con la siguiente sentencia:  

```sql
mysql>SHOW GRANTS FOR user;
```
<p align="center">
    <img src="img/02_show_privileges.png" width="500" height="400">
</p>


- **Asignar privilegios a un usuarios:**  

Para asignar privilegios a una cuenta usamos el comando **GRANT**, el cual permite asignar a una cuenta diferentes servicios, siendo los siguintes:  

**Globales:** otorga los privilegios a un usuario sobre todo el servidor, esto se realiza por medio de la sentencia: 

```sql
GRANT privileges ON *-* TO 'username';
```

Si queremos que el nuevo usuario tenga permisos de administrador (Todos los permisos), debemos de ejecutar la siguiente sentencia:  

```sql
GRANT ALL PRIVILEGES ON *.* TO 'username'@'localhost';
```
Los asteriscos indican que los permisos serán asignados a todas las bases de datos y a todas las tablas (primer asteriscos bases de datos, segundo asterisco tablas).

<p align="center">
    <img src="img/03_assign_privileges.png" width="500" height="400">
</p>

Si queremos asignar permisos para ciertas acciones, la sentencia quedaría de la siguiente manera. Reemplazamos ALL PRIVILEGES y colocamos las acciones que queremos asignar.


```sql
mysql>GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP
    -> ON userdb.*
    -> TO 'username'@'localhost';
```

Una vez hayamos finalizado con los permisos, el último paso será refrescarlos. 

```sql
mysql>FLUSH PRIVILEGES;
```

- **Revocar privilegios a un usuarios:**

Para borrar los privilegios de una cuenta con la sentencia:

```sql
REVOKE privileges ON*-*TO 'username';
```

Remover permisos en concreto (Ejemplo create y delete):  

```sql
REVOKE CREATE, DELETE ON *.* FROM 'username'@'localhost';
```

Remover todos los privilegios:  

```sql
REVOKE ALL PRIVILEGES ON *.* FROM 'username'@'localhost';
```

<p align="center">
    <img src="img/04_revoke_privileges.png" width="500" height="350">
</p>



- **Borrar usuarios:**  

De igual forma para crear usuarios, necesitamos  tener los permisos pertinentes para poder borrarlos. Para borrar a un usuario utilzamos la sentencia **DROP USER**:  

```sql
mysql>DROP USER user;
```

<p align="center">
    <img src="img/05_delete_user.png" width="500" height="350">
</p>
