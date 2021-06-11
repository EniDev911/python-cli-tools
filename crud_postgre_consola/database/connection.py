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
			cursor = self.conn.cursor()
			cursor.execute('SELECT * FROM libro;')
			result = cursor.fetchall()
			return result
		
		except Error as ex:
			print(f"Error trying to connect: {ex}")

	def create_book(self):
		pass
objDAO = DAO()
objDAO.get_book()