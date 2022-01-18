# ===================================== #
#    ______        _  ____              #
#   / ____/____   (_)/ __ \ ___  _   __ #
#  / __/  / __ \ / // / / // _ \| | / / #
# / /___ / / / // // /_/ //  __/| |/ /  #
#/_____//_/ /_//_//_____/ \___/ |___/   #
# ===================================== #                                     

import sqlite3
import subprocess as sp
import os


DB = 'university.db'

def create_table():
	""" DATABASE SCHEMA"""

	con = sqlite3.connect(DB)
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

# CREATE
def add_student(roll, name, phone):
	con = sqlite3.connect(DB)
	cursor = con.cursor()

	query = '''
		INSERT INTO student (roll, name, phone)
		VALUES (?,?,?);
			'''
	cursor.execute(query, (roll, name, phone))
	con.commit()
	con.close()

# READ
def get_student():
	con = sqlite3.connect(DB)
	cursor = con.cursor()

	query = '''
		SELECT roll, name, phone
		FROM student;
			'''
	cursor.execute(query)
	rows = cursor.fetchall()
	con.close()
	return rows

# SEARCH ROW
def get_student_by_roll(roll):

	con = sqlite3.connect(DB)
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
	
	con = sqlite3.connect(DB)
	cursor = con.cursor()

	query = '''
		UPDATE student
		SET name = ?, phone = ?
		WHERE roll = ?
	'''

	cursor.execute(query, (name, phone, roll))

	con.commit()
	con.close()

# DELETE
def delete_student(roll):

	con = sqlite3.connect(DB)
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


def delete_data(_id):
	delete_student(_id)

if os.name == "posix":
   var = "clear"       
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
   var = "cls"
 
def select():

	sp.call(var, shell=True)
	sel = input('1.Add data\n2.Show Data\n3.Search\n4.Update\n5.Delete\n6.Exit\n\n')

	if sel == '1':
		sp.call(var, shell=True)
		id_ = int(input('id: '))
		name = input('name: ')
		phone = input('phone: ')
		add_data(id_,name,phone)

	elif sel == '2':
		sp.call(var, shell=True)
		show_data()
		input('\n\npress enter to back:')

	elif sel == '3':
		sp.call(var, shell=True)
		id__ = int(input('Enter id: '))
		show_data_by_id(id__)
		input('\n\npress enter to back:')

	elif sel == '4':
		sp.call(var, shell=True)
		id__ = int(input('Enter id: '))
		show_data_by_id(id__)
		print()
		name = input('Name: ')
		phone = input('Phone: ')
		update_student(id__,name,phone)
		input('\n\nYour data has been updated \npress enter to back:')

	elif sel == '5':
		sp.call(var, shell=True)
		show_data()
		id__ = int(input('Enter id: '))
		delete_data(id__)
		input('\n\npress enter to back:')

	else:
		return 0;

	return 1;

while(select()):
	pass





