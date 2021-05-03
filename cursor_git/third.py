"""third task"""
class Person:
    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex

    def __repr__(self):
        return str([self.name, self.last_name, self.age, self.sex, self.address, self.phone_number, self.email])

andrew = Person('Andrew', 'Tsap', '0638719474', 'Lviv, Horodotska 12', 'tsapandre12@gmail.con', '23-04-1996', '25', 'male')
print(repr(andrew))