import connection as conn
from prettytable import PrettyTable

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
	id = int(input('Enter id of record:\n'))
	record = db.run_query('SELECT * FROM contacts WHERE id={}'.format(id))
	record = record.fetchone()
	
	if id == record[0]:
		#sql = 'DELETE FROM contacts WHERE id=?'
		#db.run_query(sql, (id,))
		print(f'Are you sure delete to {record[1]}')

while True:

	print(":=="*20)
	print("\t\tCONSOLE CRUD WITH SQLITE3")
	print(":=="*20)
	print("[C]reate new Database")
	print("[D]rop Database")
	print("[U]se Database")
	print("[E]xit")


	try:
		opt = input('Select one option:\n')

		if opt.upper() == 'C':
			db.createDB()

		elif opt.upper() == 'D':
			db.dropDB()

		elif opt.upper() == 'U':

			while True:

				print("[1] Insert a row")
				print("[2] Show all row")
				print("[3] Update a row")
				print("[4] Delete a row")
				print("[5] Search a row")
				print("[6] Exit")
				print(":=="*20)
				try:
					option = int(input('Select one option:\n'))

					if option == 1:
						create()
					if option == 2:
						get()
					if option == 3:
						update()
					elif option  == 4:
						delete()

					elif option == 6:
						break

				except:
					print('Option invalid!')	


		elif opt.upper() == 'E':
			break

	except:
		print('Option invalid!')