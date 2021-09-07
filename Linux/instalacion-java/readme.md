
La licencia de OracleJDK ha cambiado para los lanzamientos a partir del 16 de abril de 2019.  

El nuevbo acuerdo de Oracle Technology Network para Oracle Java SE es sustancialmente diferente de las licencias anteriores de Oracla JDK. La nueva licencia permite ciertos usos, como el uso personal y el uso de desarrollo, sin costo alguno, pero es posible que otros usos autorizados bajo licencias anteriores de oracle JDK ya no estén disponibles.  


1. **Actualización de paquetes**  

Para poder actualizar los paquetes de java debemos remover el PPA web8updteam desde Synaptic, hacemos el proceso desde la terminal con <kbd>CTRL</kbd> + <kbd>T</kbd>  

**Removemos el PPA**  

```bash
sudo add-apt-repository -r ppa:webupd8team/java
```

**Actualizamos el índice de base de datos** 

```bash
sudo apt update
```

**Volvemos agregar el PPA**  

```bash
sudo add-apt-repository ppa:webupd8team/java
```


**Actualizamos nuevamente** 

```bash
sudo apt update
```

**Instalamos OracleJdk 8**

```
sudo apt install oracle-java8-installer
```


