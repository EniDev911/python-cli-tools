import connection as conn
from prettytable import PrettyTable
import os

db = conn.Database()

def get():
	table = PrettyTable()
	table.field_names = ['id', 'Name', 'Phone', 'Email']
	table.align['id'] = 'r'
	table.align['Name'] = 'l'
	table.align['Phone'] = 'r'
	table.align['Email'] = 'l'
	records = db.run_query('SELECT * FROM contacts')
	for row in records.fetchall():
		table.add_row(row)
	table.sortby = 'Name'
	print(table.get_string(title = 'My Contacts'))


def clear():
	platform = os.name
	if platform == 'nt':
		os.system('cls')
	else:
		os.system('clear')
    		
    		
def validations(data = ()):
	aux = 0
	for r in data:
		if len(r) > 0:
			aux += 1
	return len(data) == aux


def update():
	id = int(input('Enter id of record:\n'))
	record = db.run_query('SELECT * FROM contacts WHERE id={}'.format(id))
	record = record.fetchone()
	#res = input(f'Are you sure to update the contact {record[1]}? "yes or no"\n')  
	#if (str(res.Upper()) == 'YES' or 'Y'):
	name = str(input(f'Enter new name: (old: {record[1]})\n'))
	phone = str(input(f'Enter new phone: (old: {record[2]})\n'))
	email = str(input(f'Enter new email: (old: {record[3]})\n'))
	data = (name, phone, email)

	if validations(data):
		sql = 'UPDATE contacts SET name=?,phone=?,email=? WHERE id=?'
		db.run_query(sql, (name, phone, email, id))
		print('Record updated Succesfully')

	else:
		print('All fields are required!')
		update()
	

def create():
	name = input('Enter name:\n')
	phone = input('Enter phone:\n')
	email = input('Enter email:\n')
	data = (name, phone, email)
	
	if validations(data):
		db.run_query('INSERT INTO contacts VALUES(NULL,?,?,?)',data) 
		print('Record entered Succesfully')
	else:
		print('All fields are required')


def delete():
	id = int(input('Enter id of record: \n'))
	record = db.run_query('SELECT * FROM contacts WHERE id={}'.format(id))
	record = record.fetchone()
	
	if id == record[0]:
		#sql = 'DELETE FROM contacts WHERE id=?'
		#db.run_query(sql, (id,))
		print(f'Are you sure delete to {record[1]}?:')
		res = input('yes or no: ')
		if res.lower() == 'yes':
			sql = 'DELETE FROM contacts WHERE id=?'
			db.run_query(sql, (id,))
			print('Record deleted succesfully')

		elif res.lower() == 'no':
			clear()

