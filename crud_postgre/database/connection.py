import psycopg2

from psycopg2 import Error

class DAO:
	def __init__(self):
		try:
			self.conn = psycopg2.connect(
				host = '127.0.0.1',
				user = 'postgres',
				password = 'postgres',
				database = 'biblioteca'
			)
			print('Connectivity succesfully')

		except Error as ex:
			print(f"Error trying to connect: {ex}")

	def get_book(self):
		try:
			with self.conn.cursor() as cursor:
				cursor.execute('SELECT * FROM libro;')
				result = cursor.fetchall()
				return result
		
		except Error as ex:
			print(f"Error trying to connect: {ex}")

	def register_book(self, book):
		try:
			with self.conn.cursor() as cursor:
				sql = 'INSERT INTO libro (id, title, description) VALUES(%s,%s,%s)'
				values = (curso[0], curso[1], curso[2])
				cursor.execute(sql, values)
				self.conn.commit()
				print("¡Libro registrado!\n")

		except Error as ex:
			print(f"Error trying to connect: {ex}")

objDAO = DAO()
objDAO.get_book()