class Person:
	def __init__(self, firstName: str, lastName: str, occupation: str, age: int = 0, gender: str = "Female"):
		self.firstName = firstName
		self.lastName = lastName
		self.age = age
		self.gender = gender
		self.occupation = occupation

	def __str__(self) -> str:
		return f"{self.firstName}, {self.lastName}, {self.age}, {self.gender},{self.occupation}"
