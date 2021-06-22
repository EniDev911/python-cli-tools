class Customer:

    def __init__(self, first_name, last_name, age, city, country):
        self.first_name = first_name
        self.last_name = last_name
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
        return "Customer('{}', '{}', '{}', '{}', '{}')".format(
            self.first_name, 
            self.last_name, 
            self.age, 
            self.city, 
            self.country)

