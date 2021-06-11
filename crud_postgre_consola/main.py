from database.connection import DAO

def main_menu():
	running = True
	while(running):
		right_opt = False
		while(not right_opt):
			print("****** Menu Principal ******")
			print("[1]Listar libros")
			print("[2]Registrar un libro")
			print("[3]Actualizar un libro")
			print("[4]Eliminar un libro")
			print("[5]Salir")
			print("****************************")
			opt = int(input("Seleccione una opción presionando la tecla entre corchetes de la opción\n"))

			if opt < 1 or opt > 5:
				print("Opción incorrecta, ingrese nuevamente...")

			elif opt == 5:
				print("¡Gracias por usar este sistema!")
				running = False
				break
			else:
				run_option(opt)
				right_opt = True

def run_option(option):
	obj_dao = DAO()
	if option == 1:
		try:
			books = obj_dao.get_book()
			if len(books) > 0:
				for book in books:
					print(book)
			else:
				print('No hay registros en la base de datos aún.')			
		except:
			print('error')





main_menu()