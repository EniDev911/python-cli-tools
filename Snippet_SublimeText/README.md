## Crear Snippet  

Para poder crear un nuevo snippet Vamos a **Tools** ->**Developer**->**New Snippet** 

Se nos abrirá un nuevo archivo con el siguiente contenido en xml

```xml
<snippet>
    <content><![CDATA[
Hello, ${1:this} is a ${2:snippet}.
]]></content>
    <!-- Optional: Set a tabTrigger to define how to trigger the snippet -->
    <!-- <tabTrigger>hello</tabTrigger> -->
    <!-- Optional: Set a scope to limit where the snippet will trigger -->
    <!-- <scope>source.python</scope> -->
</snippet>
```


### Etiqueta content: 

En la etiqueta **content** es donde va el contenido de tu código, específicamente dentro de corchetes **CDATA** ahí va a estar el código que vamos a incluir.  

Las variables ${1:this} y ${2:snippet} son opcionales, funcionan para posicionar el cursor y desplazarse de una variable a otra de forma ascendente tan solo con tabular, puedes añadir todas las variables que requieras, veamos lo un poco más a fondo:

${1}: Por si solo indica que una vez el código se imprima el cursor se debe posicionar en esa posición.

:this: Este es como un texto de ayuda para indicar cuál es el texto que debería de ir allí, así que es opcional.

NOTA: Si colocas el mismo numero de variable en dos o mas lugares distintos de tu codigo con editar el primero se edita el resto.

### Etiqueta tabTrigger:

Esta es una etiqueta opcional, tal como explica la plantilla y funciona para añadir la abreviación o acceso directo del teclado a nuestro código, es decir, que con que escribamos nuestra palabra y tabulemos aparezca el contenido.

### Etiqueta scope:

Al igual que la anterior está es una etiqueta opcional y funciona para indicarle a sublime en que tipo de archivos y/o extensiones es que va a funcionar el snippet, nosotros particularmente nunca usamos esta etiqueta, ya que si creamos un snippet para html, este no va a funcionar en plantillas php y viceversa.


## Ingresar tu código en el content

Ahora que ya sabemos que es y cual es la función de cada etiqueta podemos añadir el contenido de nuestro código, veamos 2 ejemplos

**Snippet para HTML5 estructura:** 

```xml
<snippet>
    <content><![CDATA[
<!DOCTYPE html>
<html lang="es">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
        <meta name="description" content="">
        <meta name="author" content="">
        <link rel="shortcut icon" href="images/favico.ico">
        <link rel="apple-touch-icon-precomposed" href="images/favico.ico">
        <title>$1</title>
        <!-- Bootstrap core CSS -->
        <link href="css/bootstrap.min.css" rel="stylesheet">
        <script src="js/jquery.min.js"></script>
    </head><!--nextpage-->
 
    <body>
        <div class="container">
            <header>
                <!-- Static navbar -->
                <nav id="header-menu" class="navbar navbar-default">
                    $2
                </nav>
            </header>
            <!-- Main component for a primary marketing message or call to action -->
            <section>
                $3
            </section>
            <footer>
                $4
            </footer>
        </div> <!-- /container -->
 
        <!-- Bootstrap core JavaScript
        ================================================== -->
        <script src="js/jquery.min.js"></script>
        <script src="js/bootstrap.min.js"></script>
        <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    </body>
</html>
]]></content>
    <!-- Optional: Set a tabTrigger to define how to trigger the snippet -->
    <tabTrigger>html5</tabTrigger>
    <!-- Optional: Set a scope to limit where the snippet will trigger -->
    <!-- <scope>source.python</scope> -->
</snippet>
```
Salvamos los cambios guardando en el directorio de user de sublimetext con el nombre de **html5.sublime-snippet**

Ahora si creamos un nuevo archivo y escribimos html5 y presionamos el tabulador o presionado la combinación ctrl + space se nos autocompletara la estructura de html5.  


**Snippet de Python:**

```xml
<snippet>
    <content><![CDATA[
from tkinter import *
from tkinter import ttk 
from tkinter import messagebox


root = Tk()
root.title("My Application")
root.geometry("800x700")
${1}
root.mainloop()     
${2}
]]></content>
    <!-- Optional: Set a tabTrigger to define how to trigger the snippet -->
<tabTrigger>start.tk</tabTrigger>
    <!-- Optional: Set a scope to limit where the snippet will trigger -->
<scope>source.python</scope>
</snippet>
```

Este snippet exclusivamente estará disponible dentro de archivos con la extensión de python **py**
