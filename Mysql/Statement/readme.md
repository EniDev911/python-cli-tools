## Consultas Básicas  

- Desplegar el listado de bases de datos.

```sql
show databases;
```
- Seleccionar una base de datos existente para manipular.

```sql
USE <<name-database>>;
```
- Ver columnas de una tabla y sus tipo de datos.

```sql
describe <<name-table>>
```

## Administrar Usuarios

Debemos estar logueados como root o usuario con todos los privilegios  

- Crear usuario (sin privilegios)  

```sql
CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
```

- Otorgar privilegios 

```sql
GRANT ALL PRIVILEGES ON *.* TO 'username'@'localhost';
```
- Cargar la tabla de privilegios  

```sql
FLUSH PRIVILEGES;
```
