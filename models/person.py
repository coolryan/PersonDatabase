class Person:
	def __init__(self, firstName: str, lastName: str, occupation: str, age: int = 0, gender: str = "Female"):
		self.firstName = firstName
		self.lastName = lastName
		self.occupation = occupation
		self.age = age
		self.gender = gender

	def __str__(self) -> str:
		return f"{self.firstName}, {self.lastName}, {self.occupation}, {self.age}, {self.gender}"
