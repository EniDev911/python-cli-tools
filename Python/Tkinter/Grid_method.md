## El método <b>.grid()</b>  

Para mostrar un widget 'w' en la pantalla de su aplicación:  m


<code>
    w.grid(option=value,...)
</code><br>

Este método registra un widget 'w' con el administrador de geometría de cuadrícula; si no lo hace, el widget existirá internamente, pero no estará visible en la pantalla.  

Tabla. Argumentos del administrador de geometría **.grid()**  

|**opción**|Descripción|
|----------|:-----------|
|column|El número de columna donde desea que se cuadricule el widget, contando desde 0. El valor por defecto es 0|
|columnspan|Normalmente, un widget ocupa solo una celda en la cuadrícula. Sin embargo, puede tomar varias celdas de una fila y combinarlas en una celda más grande configurando la opción **columnspan** en el número de celdas. Por ejemplo, <b>w.grid(row=0, column=2, columnspan=3)</b> colocaría el widget <b>'w'</b> en una celda que abarque las columnas 2, 3 y 4 de las fila 0.|
|in_|Para registrar 'w' como hijo de algún widget. El nuevo padre debe ser descendiente del widget utilizado cuiando se creó.|
|ipadx|Espaciado **x** interno. Esta dimensión se agrega dentro del widget dentro de sus lados izquierdo y derecho.|
|ipady|Espaciado **y** interno