class Address:
	def __init__(self, streetAddress: str, city: str, state: str, zipCode: str, id: int = None):
		self.id = id
		self.streetAddress = streetAddress
		self.city = city
		self.state = state
		self.zipCode = zipCode

	def __str__(self) -> str:
		return f"{self.id, self.streetAddress, self.city, self.state, self.zipCode}"
