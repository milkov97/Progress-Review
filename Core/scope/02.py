# What will be the output of the following code? Why?
x = 10

def outer_function():
    x = 5

    def inner_function():
        x = 2
        print(x)

    inner_function()
    print(x)

outer_function()