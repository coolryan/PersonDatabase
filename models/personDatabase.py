import sqlite3
from models.person import Person
class PersonDatabase:
	def __init__(self):
		try:
			# Create a database called person.db and then connect to the DB
			# and create a cursor- for instance: 'c' stands for cursor
			sqliteConn = sqlite3.connect('person.db')
			c = sqliteConn.cursor()
			print('The DB is connected successfully')

			# Write a query execution by creating a table called person
			c.execute("""CREATE TABLE IF NOT EXISTS person(
				ID INTEGER PRIMARY KEY AUTOINCREMENT,
				FIRSTNAME TEXT NOT NULL,
				LASTNAME TEXT NOT NULL,
				AGE INTEGER NOT NULL,
				GENDER TEXT NOT NULL,
				OCCUPATION TEXT NOT NULL
			)""")

			sqliteConn.commit()
		# Handle errors
		except sqlite3.Error as e:
			print('Error occured - ', e)

		# Close DB Connection irrespective of success
		# or failure
		finally:
			if sqliteConn:
				sqliteConn.close()
				print('SQLite Connection is closed')

	def createPerson(self, person: Person):
		# Create a database called person.db and then connect to the DB
		# and create a cursor- for instance: 'c' stands for cursor
		try:
			sqliteConn = sqlite3.connect('person.db')
			c = sqliteConn.cursor()
			print('The DB is connected successfully')

			# Write a query execution where to insert the values into 'person' table
			c.execute("""INSERT INTO person (FIRSTNAME, LASTNAME, AGE, GENDER, OCCUPATION) 
				VALUES (?, ?, ?, ?, ?)""", (person.firstName, person.lastName, person.age, person.gender, person.occupation))

			# Fetch and output the result
			result = c.fetchall()
			for result in c.execute('SELECT * FROM person'):
				print('The result of this database is {}'.format(result))

			sqliteConn.commit()

		# Handle errors
		except sqlite3.Error as e:
			print('Error occured - ', e)

		# Close DB Connection irrespective of success
		# or failure
		finally:
			if sqliteConn:
				sqliteConn.close()
				print('SQLite Connection is closed')


