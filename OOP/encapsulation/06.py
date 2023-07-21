# What will be the output of the following code? Why?
class Person:

    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value < self.age:
            raise ValueError(f'Age must be bigger than {self.age}')
    
    def introduce(self):
        return f'Hi my name is {self.name} and I am {self.age} years old.'
    
p = Person('Ivan', 21)

# After one year, on Ivan's birthday, we need to update his age.
p._age = 20
print(p.introduce())