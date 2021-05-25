from .contact import Contact
from .dbcsv import DBbyCSV
import csv

SCHEMA = {
    'ID': {
        'type': 'autoincrement',
    },
    'NAME': {
        'type': 'string',
        'min_length': 3,
        'max_length': 50
    },
    'SURNAME': {
        'type': 'string',
        'min_length': 5,
        'max_length': 100
    },
    'EMAIL': {
        'type': 'string',
        'max_length': 254
    },
    'PHONE': {
        'type': 'int'
    },
    'BIRTHDAY': {
        'type': 'date'
    }
}

class DBContacts(DBbyCSV):

    def __init__(self):
        super().__init__(SCHEMA, 'contacts')



    def save_contact(self, contact):
        data = [contact.name, contact.surname, contact.email, contact.phone, contact.birthday]
        return self.insert(data)



    def get_all(self):

        list_data = []
        list_header = []

        with open(self._filename, mode='r', encoding='utf-16') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            is_header = True

            for row in csv_reader:
                    list_header = row
                    is_header = False
                    continue

            if row:
                file = {}
                for key, value in enumerate(row):
                    file[list_header[key]] = value

                list_data.append(file)

        return list_data





    def list_contact(self):
        list_contacts = self.get_all()

        if not list_contacts:
            return None

        object_contacts = []

        # Convertimos los datos a objetos de tipo contact
        for contact in list_contacts:
            c = Contact(contact['ID'], contact['NAME'], contact['SURNAME'],contact['EMAIL'], contact['PHONE'], contact['BIRTHDAY'])
            object_contacts.append(c)

        return object_contacts

    def get_schema(self):
        return SCHEMA

    def insert(self, data):
        id_contact = self.get_last_id() + 1
        line = [id_contact] + data


        with open(self._filename, mode = 'a', encoding='utf-16') as csv_file:
            data_writer = csv.writer(csv_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL,
                lineterminator='\n')

            data_writer.writerow(line)

        return True



    def get_last_id(self):

        list_ids = []
        with open(self._filename, mode='r', encoding='utf-16') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            is_header = True
            for row in csv_reader:
                if is_header:
                    is_header = False
                    continue

                if row:
                    list_ids.append(row[0])

        if not list_ids:
            return 0

        list_ids.sort(reverse = True)
        return int(list_ids[0])


