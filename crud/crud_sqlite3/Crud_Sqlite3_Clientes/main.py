from clientes import Customer
import sqlite3

class Connection:

	def __init__(self):
		self.DB = 'customers.db'


	def run_query(self):
		with sqlite3.connect(self.DB) as conn:
			cur = conn.cursor()
			cur.execute("""
				CREATE TABLE customer(
					id INTEGER PRIMARY KEY AUTO_INCREMENY,
					fname VARCHAR(30) NOT NULL,
					lname VARCHAR(30),
					age INTEGER,
					city VARCHAR(40),
					country VARCHAR(40)
				""")
			conn.commit()
