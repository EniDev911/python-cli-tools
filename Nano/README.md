## Python syntax highlighting para Nano

Nano contiene por defecto las definiciones de sintaxys para diferentes lenguajes:  

<p align="center">
    <img src="assets/01.png">
</p>


Para habilitar el resaltado de un lenguajem agrega mediante la palabra reservada **include** y la ruta al archivo con su definición de resaltado del lenguaje que desee habilitar en su archivo **~/.nanorc**, Entonces, por ejemplo, para habilitar C / C++, agregaría esta línea: 

```bash
include include "/usr/share/nano/c.nanorc"
```

Esto debe incluir todos los complementos de resaltado de sintaxis incluidos de forma predeterminada, y todos los que agregue a **/usr/share/nano**:

```bash
find /usr/share/nano -name '*.nanorc' -printf "include %p\n" > ~/.nanorc
```

## preview my syntax highlighting

  
<ul><li>
<a title="./highlight/enidev911.python.nanorc" href="./highlight/enidev911.python.nanorc"><strong>Enidev911_Python</strong></a>  
</li></ul>
<p align="center">
    <img src="assets/02_python.png">
</p>