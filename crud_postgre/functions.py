def get_books(books):
	print("Libros: ")
	count = 1
	for book in books:
		data = "{0}. Código: {1} | Título: {2} | Descripción: {3}\n"
		print(data.format(count, book[0], book[1], book[2]))
		count = count + 1

def get_data_register():
	cod = int(input('Ingrese código: '))
	name = input('Ingrese título del libro: ')
	description = input('Ingrese descripción del libro: ')
	book = (cod, name, description)
	return book
