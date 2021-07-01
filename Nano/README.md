## Python syntax highlighting para Nano

Nano contiene por defecto las definiciones de sintaxys para diferentes lenguajes:  

<p align="center">
    <img src="assets/01.png">
</p>


Para habilitar el resaltado de un lenguaje agrega mediante la palabra reservada **include** y la ruta al archivo con su definición de resaltado del lenguaje que desee habilitar en su archivo **~/.nanorc**, Entonces, por ejemplo, para habilitar C / C++, agregaría esta línea: 

```bash
include "/usr/share/nano/c.nanorc"
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


## Trigger events by uncommenting  

Por ejemplo algunos que vienen en el archivo **~/.nanorc**  

```txt
#bind ^Q exit all
#bind ^S savefile main
#bind ^W writeout main
#bind ^O insert main
#bind ^H help all
#bind ^H exit help
#bind ^F whereis all
#bind ^G findnext all
#bind ^B wherewas all
#bind ^D findprevious all
#bind ^R replace main
#bind M-X flipnewbuffer all
#bind ^X cut all
#bind ^C copy main
#bind ^V paste all
#bind ^P location main
#bind ^A mark main
#unbind ^K main
#unbind ^U all
#unbind ^N main
#unbind ^Y all
#unbind M-J main
#unbind M-T main
#bind ^T gotoline main
#bind ^T gotodir browser
#bind ^Y speller main
#bind M-U undo main
#bind M-R redo main
#bind ^U undo main
#bind ^E redo main
#set multibuffer
```

## Manage files  

Para poder abrir más de un archivo en el editor, se pasan estos como argumentos separados despues de llamar a nano. Ejemplo:  

```bash
nano file_1.py file_2.py
```

**Change files**  

Puedes cambiar entre archivos abiertos en el buffer con la siguiente combinación:  

**Alt+Left**  y **Alt+Right**


