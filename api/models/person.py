from models.address import Address

class Person:
	def __init__(self, firstName: str, lastName: str, occupation: str, age: int = 0, gender: str = "Female", id: int = None, address : Address = None):
		self.id = id
		self.firstName = firstName
		self.lastName = lastName
		self.age = age
		self.gender = gender
		self.occupation = occupation
		self.address = address

	def __str__(self) -> str:
		return f"{self.id}, {self.firstName}, {self.lastName}, {self.age}, {self.gender}, {self.occupation}, {self.address.streetAddress}, {self.address.city}, {self.address.state}, {self.address.zipCode}"

	def setAddress(self, address: Address):
		self.address = address

