import mysql.connector 
import os 
from dotenv import dotenv_values
from mysql.connector import errorcode
from mysql.connector import Error



#print(config)
#print(config['DBHOST'])
#print(config['DBUSER'])

# DBHOST=127.0.0.1
# DBUSER=root
# DBPASS=enidev911
# DBPORT=3306
# DBDATABASE=storeDB

class DAO:

	def __init__(self):
		"""

		"""
		config = dotenv_values()
		try:
			self.cnx = mysql.connector.connect(
				host = config['DBHOST'],
				user = config['DBUSER'],
				password = config['DBPASS'],
				db = config['DBDATABASE']
				)

			print(self.cnx)
			print(self.cnx.is_connected())

		except Error as err:
			if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
				print("Error with your credentials to connect")

			if err.errno == errorcode.ER_BAD_DB_ERROR:
				print("Dabatase not exists")
		

	def run_query(self, query):
		if self.cnx.is_connected():
			cursor = self.cnx.cursor()
			cursor.execute(query)
			result = cursor.fetchall()
			return result
db = DAO()
result = db.run_query('SELECT * FROM books;')
print(result)


