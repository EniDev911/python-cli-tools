## Solicitar números hasta que se introduzca un negativo.  

Antes que nada vamos a declarar la lista en donde vamos a ir almacenando los números. Luego haremos un ciclo while infinito que se va a romper únicamente **cuando el número sea negativo**.. 

El código queda muy simple. Primero solicitamos el número y lo convertimos a flotante con **float**, luego agregaremos a la lista con **append**  

```python
lista = []

while True:
    numero = float(
            input("Ingrese un número (ingresa un negativo para terminar): ")
            )
    if numero >= 0:
        lista.append(numero)
    else:
        break
print(lista)
```

Fijate en que la condición de salida es que el número sea menor que 0, ya que en ese caso rompemos el ciclo con **break** 


## Convertir decimal a hexadecimal  

Veamos como convertir un número decimal en base 10 a un número hexadecimal en base 16. 

**Algoritmo**  

Lo que debemos hacer son divisiones mientras el número decimal sea mayor que cero. Primero obtenemos el residuo de **dividir al decimal entre 16**  
Una vez que tenemos el residuo (que será un valor entre 0 y 15) obtenemos su verdadero valor, recuerda que en hexadecimal existen las letras desde la **A** hasta la **F**, asi que si el número es mayor a 9 **se debe convertir a letra.**  

Luego, ese dígito hexadecimal es agregado al inicio de la cadena que guardará el número hexadecimal completo. Y finalmente asignamos a decimal el valor de dividirlo a sí mismo entre 16 (de este modo el ciclo se romperá en algún momento).  

Por cierto, es importante **convertir la división de decimal entre 16 a entero**, ya que necesitamos solo valores enteros porque el residuo ya lo calculamos anteriormente.  


**Código de la función**  

Necesitamos dos funciones. Una de ellas es para obtener el verdadero valor hexadecimal, y la otra es la que realmente convierte el número **decimal a hexadecimal en Python.** Como sea, el código fuente de ambas se ve así:  

```py
def obtener_caracter_hexadecimal(valor):
    valor = str(valor)
    equivalencias = {
        "10":"a",
        "11":"b",
        "12":"c",
        "13":"d",
        "14":"e",
        "15":"f",
        }
    if valor in equivalencias:
        return equivalencias[valor]
    else:
        return valor

def decimal_a_hexadecimal(decimal):
    hexadecimal = ""
    while decimal > 0:
        residuo = decimal % 16
        verdadero_caracter = obtener_caracter_hexadecimal(residuo)
        hexadecimal = verdadero_caracter + hexadecimal
        decimal = int(decimal/16)
    return hexadecimal
```


## Obtener dígito verificador  
El **algoritmo para obtener el dígito verificador** corresponde al método para validar el RUN o RUT. El Rol Único Nacional(RUN) y el Rol Único Tributario(RUT) chilenos (ambos coinciden en el RUN si se trata de personas naturales) poseen un dígito verificador que evita engaños y suplantaciones de identidad.  

El dígito verificador se obtiene a partir de un algoritmo conocido como *Módulo 11.* Existen otras maneras de obtener el dígito verificador de los números de identificación del mundo, pero en **Chile** se aplica exclusivamente el Módulo 11. El Módulo 11 consiste en la aplicación de operaciones aritméticas a cada dígito del número del RUT.  

**Procedimiento para obtener el dígito verificador**  

El RUT consta de dos partes: el número y el dígito verificador separados por un guion.  En el siguiente ejemplo se toma como RUT el número 30.686.957-X, donde 30.686.957 es el número del RUT y X es el dígito verificador que no conocemos o que queremos verificar.  

- Se procede a tomar el número de RUT de derecha a izquierda, multiplicando cada dígito por los números que componen la serie numérica **2,3,4,5,6,7;** y sumando el resultado de estos productos. Si se ha aplicado la serie hasta el final y quedan dígitos por multiplicar, se comienza la serie nuevamente:  

**7**x2=14,  
**5**x3=15,  
**9**x4=36,
**6**x5=30,
**8**x6=48,  
**6**x7=42,  
**0**x2=0,  
**3**x3=9,  

entonces la suma de los productos es: 14+15+36+30+48+42+0+9 = **194**  

Al número obtenido por la suma del producto de cada dígito por la serie ya mencionada, se le aplica el **módulo 11**, o sea se divide en 11 y se determina el resto de la división:  

parte entera de (**194**:11) = 17  
resto de la división entera: **194**-(11*<b>17</b>)











