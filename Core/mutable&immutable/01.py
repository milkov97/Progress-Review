# What will be the output of the following code? Why?

def my_function(my_list=[]):
    my_list.append(1)
    return my_list

print(my_function())
print(my_function()) 