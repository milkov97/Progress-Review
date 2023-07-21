# What will be the output of the following code? Why?
x = 10

def outer_function():
    x = 5

    def inner_function():
        x = 2
        return x

    inner_function()
    return x


print(x)
outer_function()
print(x)
