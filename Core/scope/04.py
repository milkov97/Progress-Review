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
