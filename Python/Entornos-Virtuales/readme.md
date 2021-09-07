## Entorno Virtuales  

Python 3.3 y posteriores ya incluyen un módulo estándar **venv** para trabajar con un entorno virtual.

nota: En algunos sistemas linux no viene instalado para instalar usa el siguiente comando:  

```bash
sudo apt install python3-venv
```

**Crear un entorno virtual llamado tuto-venv**  

Ve a la carpeta donde quieras crear el entorno virtual, y ejecuta el siguiente comando dentro de la carpeta seleccionada.

```bash
python3 -m venv tuto-venv
```
**Activar el entorno virtual**  

```bash
## Windows
.\tuto-venv\Script\activate
## Linux - Mac
source tuto-env/bin/activate
```

**Desactivar el entorno** 

```bash
deactivate
```



