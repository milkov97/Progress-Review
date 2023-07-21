# What will be the output of the following code? Why?
class A:
    def method(self):
        print("Method of A")

class B(A):
    def method(self):
        print("Method of B")

class C(A):
    def method(self):
        print("Method of C")

class D(B, C):
    pass

d = D()
d.method()