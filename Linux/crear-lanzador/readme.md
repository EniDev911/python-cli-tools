**Lo primero es abrir tu editor de preferencia y crear un archivo .desktop**

Este archivo lo crearemos en la carpeta home/usr/share/applications (obligatorio usar sudo, necesitamos permisos).

A continuación, editaremos el archivo que estemos creando. Debemos añadir las siguientes líneas:  

```
[Desktop Entry]
Name=Nombre programa
Comment=Comentario sobre el programa
Exec=/home/usuario/carpetaPrograma/bin/programa.sh
Icon=/home/usuario/Images/IconoPrograma
Terminal=false
Type=Application
```

Un ejemplo vamos a crear un lanzador para el IDE ST4 (SpringTools)

