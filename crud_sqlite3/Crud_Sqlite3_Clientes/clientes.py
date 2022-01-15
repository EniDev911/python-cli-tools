
	def __init__(self, f_name, l_name, age, city, country):
		self.first_name = f_name
		self.last_name = l_name
		self.age = age
		self.city = city
		self.country = country

	@property
	def email(self):
		return '{}.{}@gmail.com'.format(self.first_name, self.last_name)

	@property
	def fullname(self):
		return '{} {}'.format(self.first_name, self.last_name)

	def __repr__(self):
		return "Cliente ('{}', '{}', '{}', '{}', '{}')".format(
			self.first_name,
			self.last_name,
			self.age,
			self.country)

