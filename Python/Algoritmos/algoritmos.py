## Solicitar numeros hasta que sea negativo 
"""
lista = []

while True:
	numero = float(
			input("ingrese un número (coloque un negativo para terminar):\n")
			)

	if numero >= 0:
		lista.append(numero)

	else:
		break

print(lista)
"""

## convertir decimal a hexadecimal 

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

decimal = int(
    input("Escribe un número decimal, yo lo convertiré a hexadecimal: "))
hexadecimal = decimal_a_hexadecimal(decimal)

print(f"El decimal {decimal} es {hexadecimal} en hexadecimal")