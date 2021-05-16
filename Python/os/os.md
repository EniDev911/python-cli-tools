## Módulo OS  

Este módulo provee una manera versátil de usar funcionalidades depndiente del sistema operativo.  

- **os.name**  
  
El nombre del módulo dependiente del sistema operativo importado. Los siguientes nombres están registrados: *'posix', 'nt', 'java', 'os2', 'ce','riscos'*.

ejemplo:

```py
>>>import os
>>>os.name
'nt'
```
---

ejemplo para limpiar consola chequeando el valor **os.name**:  

```py
import os 

def clear():
    if os.name == 'nt':
        # Windows
        os.system('cls')
    else:
        # Linux o Mac
        os.system('clear')
clear()
```
---


- **os.environ, os.getenv(key)y os.putenv(key, value)**

El valor de **os.environ** se conoce como un objeto de mapeo que devuelve un diccionario de las **variables de entorno del usuario**. Al tratarse de un diccionario puede acceder a las variables de entorno utilizando sus métodos habituales.  

Aquí un ejemplo: 

```py
>>>print(os.environ['TMP'])
'C:\\Users\\user\\AppData\\Local\\temp'
>>># Otra forma
>>>os.getenv('TMP')
'C:\\Users\\user\\AppData\\Local\\temp'
```
---  

El beneficio de usar **os.getenv()** en lugar del diccionario **os.environ**  
es que si intenta acceder a una variable de entorno que no existe.  
la función **os.getenv()** simplemente devolverá **None**, si lo hicieramos con **os.environ** recibiremos un **raise KeyError (key)**.  

**os.putenv(key, value)**Establece la variable de entorno llamada key con el valor de la cadena value. Dichos cambios en el entorno impactan a los subprocesos iniciados con **os.system()**, **popen()** o **fork()** y **execv()**.  

---

- **os.chdir() y os.getcwd()**  
La función **os.chdir** nos permite cambiar de directorio en el que estamos ejecutando nuestra sesión de Python, Si realmente desea saber en que ruta se encuentra actualmente, debe llamar a **os.getcwd**  

```py
>>>os.getcwd()
'C:\\Python3'
>>>os.chdir(r'C:\Users\user\Documents')
>>>os.getcwd()
'C:\\Users\\user\\Documents'
```
---

Python contempla los **raw string**, en los que los caracteres se ponen tal cual y no se interpreta ninguno, por lo que no hace falta "escapar" ninguno en la siguiente línea:  


```py
>>>os.chdir(r'C:\Users\user\Documents')
```
---  







