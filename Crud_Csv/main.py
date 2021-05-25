import os
import time
from classes.contact import Contact
from classes.dbcontacts import DBContacts
from classes.validations import Validations
from prettytable import PrettyTable

validator = Validations()
db = DBContacts()

def print_option():
	print('Agenda de contacto')
	print('*'*50)
	print('Selecciona una opción')
	print('[C]rear un contacto')
	print('[L]istado de contactos')
	print('[M]odificar un contacto')
	print('[B]uscar contacto')
	print('[S]alir')

def run():
    print_option()

    option = input()
    option = option.upper()

    if option == 'C':
        create_contact()

    elif option == 'L':
        list_contact()


## Funciones de las opciones

def check_contact_data(message, data_name):
    print(message)
    input_data = input()
    try:
        getattr(validator, f'validate{data_name.capitalize()}')(input_data)
        return input_data
    except ValueError as err:
        print(err)
        check_contact_data(message, data_name)

def create_contact():
    print('CREACIÓN DE CONTACTO')
    print('*' * 50)
    name = check_contact_data('Inserta el nombre:', 'name')
    surname = check_contact_data('Inserta los apellidos:', 'surname')
    email = check_contact_data('Inserta el email:', 'email')
    phone = check_contact_data('Inserta el teléfono (9 cifras sin guiones ni puntos):', 'phone')
    birthday = check_contact_data('Inserta la fecha de nacimiento (YYYY-MM-DD):', 'birthday')

    contact = Contact(None, name, surname, email, phone, birthday)

    if db.save_contact(contact):
    	print('Contacto guardado con éxito')
    else:
    	print('Error al guardar el contacto')


def list_contact():

    list_contact = db.list_contact()

    if not list_contact:
        return print('Todavía no hay contactos guardados')

    table = PrettyTable(db.get_schema().keys())

    for contact in list_contact():
        table.add_row([
            contact.id_contact,
            contact.name,
            contact.surname,
            contact.email,
            contact.phone,
            contact.birthday
        ])

    print(table)
    print('Pulsa intro para salir')
    command = input()




if __name__ == '__main__':
	run()
