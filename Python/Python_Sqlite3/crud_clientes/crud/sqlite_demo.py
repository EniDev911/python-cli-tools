import sqlite3
from customer import Customer

connection = sqlite3.connect('customer.db')

cursor = connection.cursor()

#cursor.execute("""
#    CREATE TABLE IF NOT EXISTS customer(
#        first_name text,
#        last_name text,
#        age integer,
#        city text, 
#        country text)
#    """)
#cursor.execute("INSERT INTO customer VALUES('marco', 'contreras', 30, 'coquimbo', 'Chile')")
#cursor.execute("INSERT INTO customer VALUES('mauricio', 'larrea', 20, 'iquique', 'Chile')")
#cursor.execute("INSERT INTO customer VALUES('franco', 'mora', 15, 'santiago', 'Chile')")
#cursor.execute("INSERT INTO customer VALUES('luis', 'parra', 18, 'antofagasta', 'Chile')")
#cursor.execute("SELECT * FROM customer")
#for row in cursor.fetchmany(3):
#	print(row)

#customer_1 = Customer('fernando', 'balmaceda', 31, 'iquique', 'Chile')
#customer_2 = Customer('javier', 'zarricueta', 29, 'iquique', 'Chile')
#customer_3 = Customer('pablo', 'maldonado', 22, 'iquique', 'Chile')

# No recomendado
#cursor.execute("INSERT INTO customer VALUES ('{}','{}',{},'{}','{}')".format(
#		customer_1.first_name,
#		customer_1.last_name,
#		customer_1.age,
#		customer_1.city,
#		customer_1.country))
# Recomendado
#cursor.execute("INSERT INTO customer VALUES (?,?,?,?,?)",
#            (customer_2.first_name, customer_2.last_name,
#             customer_2.age,customer_2.city,
#             customer_2.country))
# Otra forma
#cursor.execute("INSERT INTO customer VALUES (:first, :last, :age, :city, :country)",
#				{'first':customer_3.first_name,
#				 'last':customer_3.last_name,
#				 'age':customer_3.age,
#				 'city':customer_3.city,
#				 'country':customer_3.country})


# Operaciones crud con administradores de contexto

#customer_4 = Customer('pedro', 'ossio', 25, 'puerto mont', 'Chile')
#customer_5 = Customer('sebastián', 'miranda', 27, 'valparaiso', 'Chile')
#customer_6 = Customer('adel', 'martínez', 34, 'valparaiso', 'Chile')
#print(customer_6.email)
#print(customer_6.fullname)
#print(customer_6)

# Create
#def create_customer(customer):
#    with connection:
#        cursor.execute("INSERT INTO customer VALUES(:first,:last,:age, :city,:country)",
#            {'first':customer.first_name,
#             'last':customer.last_name,
#             'age':customer.age,
#             'city':customer.city,
#             'country':customer.country})

# Get
#def get_customers(country):
#    cursor.execute("SELECT * FROM customer WHERE country=:country", {'country':country})
#    return cursor.fetchall()

# Update
#def update_city(customer, city):
#    with connection:
#        cursor.execute("""UPDATE customer SET city=:city
#            WHERE first_name=:first AND last_name=:last""",
#            {'first': customer.first_name, 'last': customer.last_name,
#             'city':city})

# Delete
#def delete_city(customer):
#    with connection:
#        cursor.execute("""DELETE FROM customer
#            WHERE first_name=:first AND last_name=:last""",
#            {'first': customer.first_name, 'last': customer.last_name})


# Added obj to database
#create_customer(customer_4)
#create_customer(customer_5)
#create_customer(customer_6)


# Update a customer
#update_city(customer_6, 'calama')

# Delete a customer
#delete_city(customer_5)


# show rows of the database
#customers = get_customers('Chile')
#for row in customers:
#	print(row)


#connection.commit()
#connection.close()