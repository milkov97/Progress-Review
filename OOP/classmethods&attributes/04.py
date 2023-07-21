# What will be the output of the following code? Why?
class MyClass:

    class_attr = 0

    @classmethod
    def change_class_attr(cls):
        cls.class_attr = 10

    
obj1 = MyClass()
obj1.change_class_attr()


obj2 = MyClass()
print(obj1.class_attr)
print(obj2.class_attr)