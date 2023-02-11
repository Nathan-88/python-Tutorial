# A function that copies a list content to a new list without changing the content of the list
def new_in_list(my_list, idx, element):
    if (idx < 0):
        return (my_list)
    if (idx >= len(my_list)):
        return (my_list)
    else:
        new_l = my_list.copy()
        new_l[idx] = element
        return (new_l)


my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)
