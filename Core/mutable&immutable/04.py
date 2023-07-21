# What will be the output of the following code? Why?
def append_to_list(item, my_list=[]):
    my_list.append(item)
    return my_list

print(append_to_list(1))  
print(append_to_list(2, [10, 20])) 
print(append_to_list(3)) 