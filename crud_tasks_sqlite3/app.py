import sqlite3

conn = sqlite3.connect('taks.db')


def insertdata(parameters = ()):
	query = 'INSERT INTO tasks(title, description) VALUES(?,?);'
	conn.execute(query, parameters)
	conn.commit()


def deletebyid(id):
	query = 'DELETE FROM tasks WHERE id = ?;'
	conn.execute(query, id)
	conn.commit()

def updatedata(parameters=())




conn.execute('''CREATE TABLE IF NOT EXISTS tasks(
	id INTEGER NOT NULL PRIMARY KEY AU|TOINCREMENT, 
	title VARCHAR(200),
    description varchar(400)
);''')


##insertdata(('running', 'go running in the beach'))
deletebyid('2');



query = 'SELECT * FROM tasks'
for row in  conn.execute(query):
	print(row)


print('Database connected')
conn.close()
