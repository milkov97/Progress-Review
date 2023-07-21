def outer_function():
    x = 10

    def inner_function():
        x = 20

    print(inner_function())

print(outer_function())