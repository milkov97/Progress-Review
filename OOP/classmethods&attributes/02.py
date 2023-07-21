# What will be the output of the following code? Why?
class Letters:
    counter = 0

    @classmethod
    def increment(cls):
        cls.counter += 1

    def __init__(self, char: str):
        self.increment()
        self.char = char 


a = Letters('a')
b = Letters('b')
c = Letters('c')
print(a.counter)
print(b.counter)
print(c.counter)
