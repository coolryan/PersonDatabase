from models.person import Person
from models.personDatabase import PersonDatabase

personDB = PersonDatabase()

def runPersonDatabase():
	for i in range(1):
		userInput = inputUser()
		person = createPerson(*userInput)
		print(person)
		personDB.createPerson(person)

def inputUser():
	firstName = input("What is the users first name: ")
	lastName = input("What is the users last name: ")
	age = input("What is the users age: ")
	gender = input("What is the users gender: ")
	occupation = input("What is the users occupation: ")
	return firstName, lastName, occupation, age, gender

def createPerson(firstName: str, lastName: str, age: int, gender: str, occupation: str) -> Person:
	return Person(firstName, lastName, occupation, age, gender)

if __name__ == "__main__":
	runPersonDatabase()
