# imports
import sqlite3
import subprocess as sp
import os


"""
database code
"""

db = 'university'

def create_table():
	con = sqlite3.connect(db)
	cursor = con.cursor()
	
	query = '''
		CREATE TABLE IF NOT EXISTS student(
			id INTEGER PRIMARY KEY,
			roll INTEGER,
			name TEXT,
			phone TEXT
			)
	'''

	cursor.execute(query)
	con.commit()
	con.close()


def add_student(roll, name, phone):
	con = sqlite3.connect(db)
	cursor = con.cursor()

	query = '''
		INSERT INTO student (roll, name, phone)
		VALUES (?,?,?)
	'''

	cursor.execute(query, (roll, name, phone))
	con.commit()
	con.close()

# get data
def get_student():
	con = sqlite3.connect(db)
	cursor = con.cursor()

	query = '''
		SELECT roll, name, phone
		FROM student
		'''

	cursor.execute(query)

	rows = cursor.fetchall()

	con.close()

	return rows

def get_student_by_roll(roll):
	con = sqlite3.connect(db)
	cursor = con.cursor()

	query = '''
		SELECT roll, name, phone
		FROM student
		WHERE roll = {}
		'''.format(roll)

	cursor.execute(query)

	rows = cursor.fetchall()

	con.close()

	return rows



def update_student(roll, name, phone):
	con = sqlite3.connect(db)

	cursor = con.cursor()

	query = '''
		UPDATE student
		SET name = ?, phone = ?
		WHERE roll = ?
	'''

	cursor.execute(query, (name, phone, roll))

	con.commit()
	con.close()


def delete_student(roll):
	con = sqlite3.connect(db)

	cursor = con.cursor()

	query = '''
		DELETE
		FROM student
		WHERE roll = {}
		'''.format(roll)

	cursor.execute(query)
	rows = cursor.fetchall()
	con.commit()

	con.close()

	return rows



create_table()


''' 

main code


'''


def add_data(id_, name, phone):
	add_student(id_, name, phone)

def get_data():
	return get_student()

def show_data():
	students = get_data()
	for student in students:
		print(student)

def show_data_by_id(id_):
	students = get_student_by_roll(id_)
	if not students:
		print('No data found at roll', id_)
	else:
		print(students)

def select():
	sp.call('clear', shell=True)
	sel = input('1.Add data\n2.Show Data\n3.Search\n4.Update\n5.Delete\n6.Exit\n\n')

	if sel == '1':
		sp.call('clear', shell=True)
		id_ = int(input('id: '))
		name = input('name: ')
		phone = input('phone: ')
		add_data(id_,name,phone)


	elif sel == '2':
		sp.call('clear', shell=True)
		show_data()
		input('\n\npress enter to back:')

	elif sel == '3':
		sp.call('clear', shell=True)
		id__ = int(input('Enter id: '))
		show_data_by_id(id__)
		input('\n\npress enter to back:')

	elif sel == '4':
		sp.call('clear', shell=True)
		id__ = int(input('Enter id: '))
		show_data_by_id(id__)
		print()
		name = input('Name: ')
		phone = input('Phone: ')
		update_student(id__,name,phone)
		input('\n\nYour data has been deleted \npress enter to back:')

	else:

		return 0;

	return 1;

while(select()):
	pass





