ID de proceso del servidor para un SqlConnection
Microsoft.Data.SqlClient v2.1 introduce una nueva SqlConnectionpropiedad ServerProcessId, en una conexión activa.

```csharp
public class SqlConnection
{
    // Retornar el id del proceso en el servidor (SPID) de la conexión activa
    public int ServerProcessId;
}
```
## Anulaciones de conexiones abierta  

El comportamiento predeterminado de **SqlConnection.Open()** se puede anular para deshabilitar el retraso de diez segundo y los reitentos de conexión automáticos provocados por errores transitorios.  


```csharp
using SqlConnection sqlConnection = new SqlConnection("Data Source=(local);Integrated Security=true;Initial Catalog=AdventureWorks;");
sqlConnection.Open(SqlConnectionOverrides.OpenWithoutRetry);
```
