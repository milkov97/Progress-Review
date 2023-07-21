class Person:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self.age = value
    
    def introduce(self):
        return f'Hi my name is {self.name} and I am {self.age} years old.'
    
p = Person('Ivan', 21)
# After one year, on Ivan's birthday, we need to update his age.
p.age = 22
print(p.introduce())
