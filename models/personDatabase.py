import sqlite3
from models.address import Address
from models.person import Person
class PersonDatabase:
	def __init__(self):
		try:
			# Create a database called person.db and then connect to the DB
			# and create a cursor- for instance: 'c' stands for cursor
			sqliteConn = sqlite3.connect('person.db')

			c = sqliteConn.cursor()

			# Write a query execution by creating a table called address
			c.execute('''CREATE TABLE IF NOT EXISTS personAddress(
				ID INTEGER PRIMARY KEY AUTOINCREMENT,
				STREETADDRESS TEXT NOT NULL,
				CITY TEXT NOT NULL,
				STATE TEXT NOT NULL,
				ZIPCODE TEXT NOT NULL
				)''')

			# Write a query execution by creating a table called person
			c.execute('''CREATE TABLE IF NOT EXISTS person(
				ID INTEGER PRIMARY KEY AUTOINCREMENT,
				FIRSTNAME TEXT NOT NULL,
				LASTNAME TEXT NOT NULL,
				AGE INTEGER NOT NULL,
				GENDER TEXT NOT NULL,
				OCCUPATION TEXT NOT NULL,
				HOMEADDRESSID INTEGER DEFAULT NULL,
				FOREIGN KEY (HOMEADDRESSID) REFERENCES personAddress (ID)
			)''')

			sqliteConn.commit()
		# Handle errors
		except sqlite3.Error as error:
			print('Error occured - ', error)

		# Close DB Connection irrespective of success
		# or failure
		finally:
			if sqliteConn:
				sqliteConn.close()

	def createAddress(self, address: Address):
		try:
			sqliteConn = sqlite3.connect('person.db')
			c = sqliteConn.cursor()

			# Write a query execution where to insert the values into 'address' table
			c.execute('''INSERT INTO personAddress (STREETADDRESS, CITY, STATE, ZIPCODE)
				VALUES (?, ?, ?, ?)''',
				(address.streetAddress, address.city, address.state, address.zipCode))

			sqliteConn.commit()

			return c.lastrowid

		# Handle errors
		except sqlite3.Error as error:
			print('Error occured - ', error)

		#Close DB Connection irrespective of success
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

			return c.lastrowid

		# Handle errors
		except sqlite3.Error as error:
			print('Error occured - ', error)

		# Close DB Connection irrespective of success
		# or failure
		finally:
			if sqliteConn:
				sqliteConn.close()

	def setPersonAddress(self, addressID: int, personID: int):
		try:
			sqliteConn = sqlite3.connect('person.db')
			c = sqliteConn.cursor()

			sql_update_query = """UPDATE person SET HOMEADDRESSID = ? WHERE ID = ?"""
			c.execute(sql_update_query, (addressID, personID))

			sqliteConn.commit()

		except sqlite3.Error as error:
			print('Failed to update sqlite table', error)
		
		finally:
			if sqliteConn:
				sqliteConn.close()

	def getAddress(self, id: int) -> Address:
		try:
			sqliteConn = sqlite3.connect('person.db')
			c = sqliteConn.cursor()

			c.execute('SELECT * FROM personAddress WHERE ID = ?', str(id)) 

			row = c.fetchone()

			if row is None:
				return None

			address = Address(id = row[0], streetAddress = row[1], city = row[2], state = row[3], zipCode = row[4])

			return address

		except sqlite3.Error as error:
			print('Error occured - ', error)

		finally:
			if sqliteConn:
				sqliteConn.close()

	def getPerson(self, id: int) -> Person:
		try:
			sqliteConn = sqlite3.connect('person.db')
			c = sqliteConn.cursor()

			c.execute('SELECT * FROM person WHERE ID = ?', id)

			row = c.fetchone()

			if row is None:
				return None

			address = self.getAddress(id = row[6])

			person = Person(id = row[0], firstName = row[1], lastName = row[2], age = row[3], gender = row[4], occupation = row[5], address = address)

			return person

		except sqlite3.Error as error:
			print('Error occured - ', error)

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
				address = self.getAddress(id = row[6])				
				person = Person(id = row[0], firstName = row[1], lastName = row[2], age = row[3], gender = row[4], occupation = row[5], address = address)
				personList.append(person)

		except sqlite3.Error as error:
			print('Error occured - ', error)

		finally:
			if sqliteConn:
				sqliteConn.close()

		return personList

	def deleteRecord(self, id: int) -> bool:
		# Create a database called person.db and then connect to the DB
		# and create a cursor- for instance: 'c' stands for cursor
		try:
			sqliteConn = sqlite3.connect('person.db')
			c = sqliteConn.cursor()

			# Deleting signle row
			sql_delete_single_query = '''DELETE FROM person WHERE ID = ?'''
			c.execute(sql_delete_single_query, id)

			sqliteConn.commit()

			if c.rowcount == 0:
				return False
			else:
				return True

		# Handle errors
		except sqlite3.Error as error:
			print('Failed to delete single record from sqlite table- ', error)
			return False

		finally:
			if sqliteConn:
				sqliteConn.close()

	def deleteAllRecords(self):
		try:
			sqliteConn = sqlite3.connect('person.db')
			c = sqliteConn.cursor()

			# Deleting multiple rows
			sql_delete_multiple_query = '''DELETE FROM person'''
			c.execute(sql_delete_multiple_query)

			sqliteConn.commit()

			print(f'Total {c.rowcount} Records deleted successfully')

		# Handle errors
		except sqlite3.Error as error:
			print('Failed to delete multiple record from sqlite table- ', error)

		finally:
			if sqliteConn:
				sqliteConn.close()
