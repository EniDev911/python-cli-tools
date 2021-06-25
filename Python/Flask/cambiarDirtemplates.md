Las plantillas de Flask, por defecto, se deben ubicar en el directorio llamado **templates**. Sin embargo, Flask permite cambiar el directorio de templates fácilmente.  

Lo único que necesitamos es, al ejecutar la app con Flask, así: 

```python
app = Flask(__name__)

Especificar el **template_folder**, así:

```python
app = Flask(__name__, template_folder=".")
```
En este caso y solo para ejemplificar, le estoy indicando a Flask que el directorio de plantillas será el mismo directorio del script(.), es decir, no hay subdirectorio; así de simple, las plantillas
viven en el mismo directorio que el script. Con **template_folder** puedes especificar cualquier ruta, incluso si es un directorio arriba o una **ruta absoluta.** 





