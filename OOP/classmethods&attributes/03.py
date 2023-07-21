# What will be the output of the following code? Why?
class MyClass:
    class_attr = 0

    @classmethod
    def class_method(cls):
        cls.class_attr += 1

    def __init__(self, value):
        self.value = value

    
    def instance_method(self):
        self.value += self.class_attr


obj1 = MyClass(10)
obj2 = MyClass(20)

obj1.class_method()
obj1.instance_method()
obj2.class_method()
obj2.instance_method()

print(obj1.value) 
print(obj2.value)