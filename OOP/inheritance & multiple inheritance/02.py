# What will be the output of the following code? Why?
class A:
    def __init__(self, val):
        self.val = val

    def method(self):
        return self.method2()

class B(A):
    def method2(self):
        return self.val

a = B(5)
print(a.method())