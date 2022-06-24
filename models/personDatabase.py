import sqlite3
from models.person import Person
class PersonDatabase:
	def __init__(self):
		try:
			# Create a database called person.db and then connect to the DB
			# and create a cursor- for instance: 'c' stands for cursor
			sqliteConn = sqlite3.connect('person.db')
			c = sqliteConn.cursor()

			# Write a query execution by creating a table called person
			c.execute('''CREATE TABLE IF NOT EXISTS person(
				ID INTEGER PRIMARY KEY AUTOINCREMENT,
				FIRSTNAME TEXT NOT NULL,
				LASTNAME TEXT NOT NULL,
				AGE INTEGER NOT NULL,
				GENDER TEXT NOT NULL,
				OCCUPATION TEXT NOT NULL
			)''')

			sqliteConn.commit()
		# Handle errors
		except sqlite3.Error as e:
			print('Error occured - ', e)

		# Close DB Connection irrespective of success
		# or failure
		finally:
			if sqliteConn:
				sqliteConn.close()

	def createPerson(self, person: Person):
		# Create a database called person.db and then connect to the DB
		# and create a cursor- for instance: 'c' stands for cursor
		try:
			sqliteConn = sqlite3.connect('person.db')
			c = sqliteConn.cursor()

			# Write a query execution where to insert the values into 'person' table
			c.execute('''INSERT INTO person (FIRSTNAME, LASTNAME, AGE, GENDER, OCCUPATION) 
				VALUES (?, ?, ?, ?, ?)''',
				(person.firstName, person.lastName, person.age, person.gender, person.occupation))

			sqliteConn.commit()

		# Handle errors
		except sqlite3.Error as e:
			print('Error occured - ', e)

		# Close DB Connection irrespective of success
		# or failure
		finally:
			if sqliteConn:
				sqliteConn.close()

	def getAllPeople(self) -> list[Person]:
		personList = []
		try:
			sqliteConn = sqlite3.connect('person.db')
			c = sqliteConn.cursor()

			# Fetch and output the result
			c.execute('SELECT * FROM person')
			rows = c.fetchall()
			for row in rows:
				person = Person(firstName = row[1], lastName = row[2], age = row[3], gender = row[4], occupation = row[5])
				personList.append(person)

		except sqlite3.Error as e:
			print('Error occured - ', e)

		finally:
			if sqliteConn:
				sqliteConn.close()

		return personList
