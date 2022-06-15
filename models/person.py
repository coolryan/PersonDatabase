class Person:
	def __init__(self, firstName, lastName, occupation, age = 0, gender = "Female"):
		self.firstName = firstName
		self.lastName = lastName
		self.occupation = occupation
		self.age = age
		self.gender = gender

	def __str__(self):
		return f"{self.firstName}, {self.lastName}, {self.occupation}, {self.age}, {self.gender}"
