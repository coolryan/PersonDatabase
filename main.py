def runPersonDatabase():
	
	for i in range(3):
		userInput = inputUser()
		personDict = createPerson(*userInput)
		print(personDict)

def inputUser():
	firstName = input("What is the users first name: ")
	lastName = input("What is the users last name: ")
	occupation = input("What is the users occupation: ")
	return firstName, lastName, occupation

def createPerson(firstName, lastName, occupation):
	return {
		"FirstName": firstName,
		"LastName": lastName,
		"Occupation": occupation,
	}

if __name__ == "__main__":
	runPersonDatabase()
