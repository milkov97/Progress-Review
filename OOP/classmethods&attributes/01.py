# What will be the output of the following code? Why?
class A:
    x = 20
    y = 30
    def __init__(self, x):
        self.x = x

a = A(40)
print(a.x)
print(A.x)
print(a.y)
print(A.y)