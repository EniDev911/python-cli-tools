
Para configurar SQL Server en Ubuntu, ejecute los siguientes comandos en una terminal para instalar el paquete **mssql-server**  

1. Importar las claves GPG del repositorio público: 

```bash
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -
# output: OK
```

2. Registre el repositorio de Ubuntu de Microsoft SQL Server para SQL Server 2019:  

Para Ubuntu 20.04:

```bash
sudo add-apt-repository "$(wget -qO- https://packages.microsoft.com/config/ubuntu/20.04/mssql-server-2019.list)"
```
Para Ubuntu 18.04:

```bash
sudo add-apt-repository "$(wget -qO- https://packages.microsoft.com/config/ubuntu/18.04/mssql-server-2019.list)"
```

3. Ejecute los siguientes comandos para comenzar la instalación de SQL Server:

```bash
sudo apt-get update
sudo apt-get install -y mssql-server
```

4. Finalizada la instalación del paquete, ejecute **mssql-conf setup** y seguimos las instrucciones para establecer el password de **SA** y elegir su edición.  

```bash
sudo /opt/mssql/bin/mssql-conf setup
```

5. Una vez realizada la configuració, verifique que el servicio se esté ejecutando:  

```
systectl status mssql-server --no-pager
```



