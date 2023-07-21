# What will be the output of the following code? Why?
class A:
    def method(self):
        return 5

class B:
    def method(self):
        return 10

class C(A, B):
    def method(self):
        return super().method() + super().method()
    
c = C()
print(c.method())