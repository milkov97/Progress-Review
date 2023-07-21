# What will be the output of the following code? Why?
def tuple_function(item, my_tuple=()):
    my_tuple += (item,)
    return my_tuple

print(tuple_function(1))
print(tuple_function(2))
print(tuple_function(3)) 


print(tuple_function(4, (10, 20)))
print(tuple_function(5)) 