from models.person import Person

def runPersonDatabase():
	for i in range(3):
		userInput = inputUser()
		personDict = createPerson(*userInput)
		print(personDict)

def inputUser():
	firstName = input("What is the users first name: ")
	lastName = input("What is the users last name: ")
	occupation = input("What is the users occupation: ")
	age = input("What is the users age: ")
	gender = input("What is the users gender: ")
	return firstName, lastName, occupation, age, gender

def createPerson(firstName: str, lastName: str, occupation: str, age: int, gender: str) -> Person:
	return Person(firstName, lastName, occupation, age, gender)

if __name__ == "__main__":
	runPersonDatabase()
