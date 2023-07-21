# What will be the output of the following code? Why?
class A:
    def __init__(self, char):
        self.char = char

    def method(self):
        return self.method2()


class B(A):
    def method2(self):
        return self.char


b = A('b')
print(b.method())