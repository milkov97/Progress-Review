class A:
    n = 10

    @classmethod
    def class_method(cls):
        return cls.n

class B(A):
    n = 20

print(B.class_method())