# a function that deletes keys with a specific value in a dictionary.
def complex_delete(a_dictionary, value):
    keys_to_delete = [k for k, v in a_dictionary.items() if v == value]
    print (keys_to_delete)
    for key in keys_to_delete:
        del a_dictionary[key]
    return a_dictionary


print_sorted_dictionary = __import__('dictionary').print_sorted_dictionary

a_dictionary = {'lang': "C", 'track': "Low", 'pref': "C", 'ids': [1, 2, 3]}
new_dict = complex_delete(a_dictionary, 'C')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)

print("--")
print("--")
new_dict = complex_delete(a_dictionary, 'c_is_fun')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)
