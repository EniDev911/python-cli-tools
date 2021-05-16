
## Crear un nuevo archivo  

<p align="center">
    <img src="img/01_new_file.png">
</p>

<p align="center">
    <img src="img/02_new_file.png">
</p>

Esto nos genera un template parecido al que se muestra a continuación:

<p align="center">
    <img src="img/03_template.png">
</p>

Vemos que tenemos texto y código r embebido

<p align="center">
    <img src="img/04_template.png" width='900' height='540'>
</p>


Veamos guardemos el documento: 

<p align="center">
    <img src="img/05_save_file.png">
</p>

Elegimos el destino, y esto comenzara a compilarse.  


Otro punto importante es que podemos elegir mostrar u ocultar el código r de la siguiente manera:  

\`\`\`{r echo=FALSE}  
summary(cars)  
\`\`\`

Poniendo el argumento **echo** en **False**  

Tambien tenemos el argumento **include** lo que hace es incluir o no el resultado y el código:  

\`\`\`{r include=TRUE, echo=FALSE}  
summary(cars)  
\`\`\`

Bien podemos separar los argumentos por una (,) consideremos que si la opción **include** esta en **FALSE** no mostrará el código aunque este la opción **echo** en **TRUE**


Tambien tenemos el argumento **eval** que su valor por defecto es True, lo que hace es evaluar si el código se evalua o no.  

<p align="center">
    <img src="img/06_eval.png">
</p>

tendriamos lo siguiente:  

<p align="center">
    <img src="img/07_eval.png">
</p>


Cabe mencionar que RMarkdown no solo es limitado para embeber código de r, sino también de otros lenguajes

