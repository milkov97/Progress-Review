def tricky_function(my_tuple=(), my_list=[]):
    my_tuple += (1,)
    my_list.append(1)
    print("Tuple:", my_tuple)
    print("List:", my_list)

tricky_function()
tricky_function() 