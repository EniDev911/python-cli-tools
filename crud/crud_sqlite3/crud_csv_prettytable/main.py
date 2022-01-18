#-------------------------------------------------------------------------------
#          Name: main
#       Version: 1.0
#         Autor: Marco Contreras
#       Support: https://www.buymeacoffee.com/9111592
#
#   Source code: https://github.com/EniDev911/PythonShell/tree/master/
#     Copyright: (c) Marco Contreras
#       Licence: GPL 3.0
#-------------------------------------------------------------------------------

import os
import time
from classes.validations import Validations
from classes.contact import Contact
from classes.dbcontacts import DBContacts
from prettytable import PrettyTable

validator = Validations()
db = DBContacts()


def print_title():
    print("                  _             _ ")      
    print("                 | |           | |")      
    print("   ___ ___  _ __ | |_ __ _  ___| |_ ___") 
    print("  / __/ _ \\| '_ \\| __/ _` |/ __| __/ __|")
    print(" | (_| (_) | | | | || (_| | (__| |_\\__ \\")
    print("  \\___\\___/|_| |_|\\__\\__,_|\\___|\\__|___/")
    print('*' * 41)

def print_option():
    print("""
   ____                     ____
  ||c ||                   ||s ||
  ||__|| [C]reate          ||__|| [S]how
  |/__\\|                   |/__\\|

        ____            ____ 
       ||e ||          ||d ||
       ||__|| [E]dit   ||__|| [D]elete
       |/__\\|          |/__\\|

               ____
              ||q ||
              ||__|| [Q]uit
              |/__\\|
   """)
    print('*' * 41)

def print_author():
    print("  ______         _  _____") 
    print(" |  ____|       (_)|  __ \\")
    print(" | |__    _ __   _ | |  | |  ___ __   __")
    print(" |  __|  | '_ \\ | || |  | | / _ \\\\ \\ / /")
    print(" | |____ | | | || || |__| ||  __/ \\ V /")
    print(" |______||_| |_||_||_____/  \\___|  \\_/")

def clear_screen():
    platform = os.name 
    if platform == 'posix':
        os.system('clear')
    elif platform == 'nt' or platform == 'ce' or platform == 'dos':
        os.system('cls')


def check_contact_data(message, data_name, force = True):

    print()
    print(message.center(41))
    input_data = input("> ".rjust(10))

    if not force and not input_data:
        return

    try:
        getattr(validator, f'validate{data_name.capitalize()}')(input_data)
        return input_data

    except ValueError as err:
        print(err)
        check_contact_data(message, data_name)


def create_contact():
    print('*' * 41)
    print('CREATE CONTACT'.center(41))
    print('*' * 41)
    name = check_contact_data("Type the contact's name:", 'name')
    surname = check_contact_data("Type the contact's last name", 'surname')
    email = check_contact_data('Type the email:', 'email')
    phone = check_contact_data('Type phone number (9 digits): ', 'phone')
    birthday = check_contact_data('Type date of birth (YYYY-MM-DD)', 'birthday')

    contact = Contact(None, name, surname, email, phone, birthday)

    if db.save_contact(contact):
        print('Contact successfully registerd')
    else:
        print('Failed to save contact')

def list_contacts():
    list_contacts = db.list_contacts()

    if not list_contacts:
        return print('No registered contacts')
    clear_screen()
    os.system("mode con: cols=73 lines=29")
    _print_table_contacts(list_contacts)


def search_contact():

    filters = {}
    print('Enter a name (empty to use another filter):')
    name = input()
    if name:
        filters['NAME'] = name

    print('Introduce un apellido (vacío para usar otro filtro):')
    apellidos = input()
    if apellidos:
        filters['SURNAME'] = apellidos
    print('Introduce un email (vacío para usar otro filtro):')
    email = input()
    if email:
        filters['EMAIL'] = email

    try:
        list_contacts = db.search_contacts(filters)
        if not list_contacts:
            return print('No hay ningún contacto con esos criterios de búsqueda')

        _print_table_contacts(list_contacts)
    except ValueError as err:
        print(err)
        time.sleep(1)
        search_contact()


def update_contact():

    list_contacts()

    print('Introduce el id del contacto que quieres actualizar:')
    id_object = input()

    data = {}
    nombre = check_contact_data('Introduce un nombre (vacío para mantener el nombre actual):', 'name', False)
    if nombre:
        data['NAME'] = nombre
    apellidos = check_contact_data('Introduce un apellido (vacío para mantener los apellidos actuales):', 'surname', False)
    if apellidos:
        data['SURNAME'] = apellidos
    email = check_contact_data('Introduce un email (vacío para mantener el email actual):', 'email', False)
    if email:
        data['EMAIL'] = email
    phone = check_contact_data('Introduce un teléfono (vacío para mantener el teléfono actual):', 'phone', False)
    if phone:
        data['PHONE'] = phone
    birthday = check_contact_data('Introduce una fecha de nacimiento YYYY-MM-DD (vacío para mantener la fecha actual):', 'birthday', False)
    if birthday:
        data['BIRTHDAY'] = birthday
    
    try:
        res = db.update(id_object, data)
        if res:
            print('Contacto actualizado con éxito')
    except Exception as err:
        print(err)
        time.sleep(1)
        update_contact()

def delete_contact():
    list_contacts()

    print('Introduce el id del contacto que quieres eliminar:')
    id_object = input()
    try:
        res = db.delete(id_object)
        if res:
            print('Contacto eliminado con éxito')
    except Exception as err:
        print(err)
        time.sleep(1)
        delete_contact()
    

def _print_table_contacts(list_contacts):
    table = PrettyTable(db.get_schema().keys())
    for contact in list_contacts:
        table.add_row([
            contact.id_contact,
            contact.name,
            contact.surname,
            contact.email,
            contact.phone,
            contact.birthday
        ])

    print(table)
    print('Pulsa cualquier letra para continuar')
    choice = input()

def run():
    os.system('color 1f')
    os.system('mode con: cols=41 lines=33')
    print_title()
    print_option()
    print()
    choice = input("(CHOICE): ".rjust(24))
    choice = choice.upper()

    
    if choice == 'C':
        clear_screen()
        create_contact()
    elif choice == 'S':
        list_contacts()
    elif choice == 'M':
        update_contact()
    elif choice == 'E':
        delete_contact()
    elif choice == 'B':
        search_contact()
    elif choice == 'Q':
        os._exit(0)
    else:
        print('\a')
        print("+".rjust(11)+"--"*9+"+")
        print("|  OPTION INVALID!".rjust(28)+'|'.rjust(2))
        print("+".rjust(11)+"--"*9+"+")


    time.sleep(1)
    run()



if __name__ == "__main__":
    run()
