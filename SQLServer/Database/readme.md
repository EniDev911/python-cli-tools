## Northwind 

Las múltiples versiones de SQL server en ocasiones nos dificultan **restaurar bases de datos .bak**  
para ello es mejor descargar y restaurar el script Notrhwinden SQL Server.  

Debido a que un archivo **.bak** es especificamente para la versión de **SQL Server que lo crea**, genera  
errores al tratar de restaurarlo en otras versiones.  

De ahí el **Managment Studio** tiene la función de **crear script de bases de datos completos**, que evitan  
incopatibilidad de versiones.  

**Northwind** es una base de datos muy conocida y bastante antigua, sin embargo, sigue siendo utilizado por  
los cursos de Microsoft.  

Para descargar el script de la bases de datos Northwind. En el siguiente enlace:  

<a href="Scripts/Northwind.sql" download="Northwind.sql">Descargar script. 💾</a> 

  
[Descargar script. 💾](Scripts/Northwind.sql)

El script contiene la información para restaurar toda la estructura de la base de datos y su contenido.  
Por lo tanto, no basta con ejecutarlo, ya que te generará un error, veamos como restaurarlo en SQL Server.  

**Restaurar script**  

Abrimos el Managment Studio del SQL Server que estemos utilizando y creamos una base de datos con el nombre **Northwind**  
abrimos una consulta y ejecutamos la siguiente instrucción:  

```sql
CREATE DATABASE Northwind;
```


