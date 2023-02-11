# a function that adds all unique integers in a list (only once for each integer)
def uniq_add(my_list=[]):
    new = []
    new = list(set(my_list))
    print(new)
    v = sum(new)
    return(v)


my_list = [1, 2, 3, 1, 4, 2, 4, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result))
