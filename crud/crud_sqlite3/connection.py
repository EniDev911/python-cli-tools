# Enidev911: https://github.com/EniDev911
import sqlite3 
import os

DB = 'database.db'

class Database:
	"""This class defines the methods to create the database and tun a query"""
	def run_query(self, query, parameters = ()):
		with sqlite3.connect(DB) as conn:
			try:
				self.cursor = conn.cursor()
				result = self.cursor.execute(query, parameters) 
				conn.commit()
				return result

			except sqlite3.OperationalError as e:
				print(e)

	def createDB(self):

		self.run_query('''
			CREATE TABLE IF NOT EXISTS contacts(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(30) NOT NULL,
            phone VARCHAR(11) NOT NULL,
            email VARCHAR(25)
            );
            ''')

		print('\t\tDATABASE CREATE SUCCESFULLY\n')


	def dropDB(self):
		if DB in os.listdir('.'):
			#os.close(DB)
			os.remove(DB)
			print('DATABASE DROP SUCCESFULLY')

