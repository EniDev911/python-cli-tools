import conexion

db = conexion.DB()

def create():
	nombre = input("Ingrese su nombre: ")
	cantidad = int(input("Ingrese una cantidad: "))
	



while True:
	print("====================")
	print("\tCRUD EN PYTHON3")
	print("====================")
	print("[1] Ingresar producto")
	print("[2] Listar productos")
	print("[3] Actualizar producto")
	print("[4] Eliminar producto")
	print("[5] Buscar producto")
	print("[6] Salir")
	print("====================")

	try:
		opcion = int(input('Seleccionar una opción\n'))

		if(opcion == 1):
			create()
		elif(opcion == 6):
			break

	except:
		print("Error en elegir las operaciones")



