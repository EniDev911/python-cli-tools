<h2 align="center">SQLCMD SQL SERVER</h2>  

<b>SQLCMD</b> es una utilidad para el manejo de bases de datos relacionales (SGBD) basado en el lenguaje <b title="Transact-SQL">T-SQL</b> mediante la línea de comandosm utilizando la línea de comandos o <b title="Command Prompt">CMD</b> podemos hacer uso de sta utilidad para:  

- Mandar instrucciones T-SQL a la base de datos SQL Server. 
- Crear scripts y procedimiento. 

**Conexión dedicada de Administración**  

<b>SQLCMD</b> también es uno de los últimos recursos cuando el sistema falla (Por ejemplo cuando la base de datos principal del sistema llamada master se corrompe). Cuando se cuelgue el sistema o que no este diponible. La conexión dedicada de administración (DAC en inglés) es uno de los recursos. <b>SQLCMD</b> permite una conexión dedicada de administración utilizando el parámetro <b>-A</b> como sigue:  

```bash
sqlcm -A
```

<b>SQLCMD</b> utiliza  el <b>OLE-DB</b> para su conexión con la base de datos. Las herramientas visuales de SQL Server como("Managment Studio", "Azure Data Studio") utiliza sqlclient para sus conexiones.  

<b>SQLCMD</b> surge como herramienta para ejecutar sentencias en T-SQL en SQLServer 2005 también incorporada en SQLServer 2008. Su antecesor es <b>Ojal</b> de la versión SQLSeerver 2000.  

<b>SQLCMD</b> puede ser utilizado como un lenguaje de programación, el paso de datos dinámicamente está permitido al igual que la interacción con scripts generados en archivos <b>.sql</b>


## Opciones de sqlcmd:  

- **opción del servidor <b>(-S)</b>: Que identifica la instancia de MSSQLServer a la que se conecta <b>SQLCMD</b> 
