def print_reversed_list_integer(my_list=[]):
    # i = len(my_list)
    # while i > 0:
    #     print("{:d}".format(my_list[i - 1]))
    #     i = i - 1
    if my_list: #checks for empty list
        for i in reversed(my_list):
            print("{:d}".format(i))
my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)
