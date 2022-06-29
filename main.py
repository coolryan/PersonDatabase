from models.person import Person
from models.personDatabase import PersonDatabase

personDB = PersonDatabase()

def runPersonDatabase():
	menu()

def inputUser():
	firstName = input("What is the users first name: ")
	lastName = input("What is the users last name: ")
	age = input("What is the users age: ")
	gender = input("What is the users gender: ")
	occupation = input("What is the users occupation: ")
	return firstName, lastName, occupation, age, gender

def createPerson(firstName: str, lastName: str, age: int, gender: str, occupation: str) -> Person:
	return Person(firstName, lastName, occupation, age, gender)

def lookUpPerson():
	id = input("Please enter an id of a person to look up: ")
	person = personDB.getPerson(id)
	print(person)

def listAllPeople():
	personList = personDB.getAllPeople()
	for person in personList:
		print(person)

def deleteSinglePerson():
	id = input("Please enter an id of a person to delete: ")
	personWasDeleted = personDB.deleteRecord(id)
	print(f"person deleted? {personWasDeleted}")

def deleteAllPeople():
	personDB.deleteAllRecords()

def menu():
	menu = {}
	menu['1'] = "Add new person"
	menu['2'] = "Look Up Person Record"
	menu['3'] = "Look Up all People"
	menu['4'] = "Delete person"
	menu['5'] = "Delete all People"
	menu['6'] = "Exit"

	shouldBreak = False

	while shouldBreak == False:
		options = menu.keys()
		for entry in options:
			print(entry, menu[entry])
		selection = input("Please Select: ")
		if selection == '1':
			userInput = inputUser()
			person = createPerson(*userInput)
			personDB.createPerson(person)
			print("person been add")
		elif selection == '2':
			lookUpPerson()
			print("person found")
		elif selection == '3':
			listAllPeople()
			print("People found")
		elif selection == '4':
			deleteSinglePerson()
		elif selection == '5':
			deleteAllPeople()
			print("people deleted")
		elif selection == '6':
			print("person database quit")
			shouldBreak = True
		else:
			print("Not valid chocie try again!")

if __name__ == "__main__":
	runPersonDatabase()
