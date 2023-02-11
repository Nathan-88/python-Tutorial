# A function that prints element in a list
def print_list_integer(my_list=[]):
        if my_list:
                for i in range(len(my_list)):
                        print("{}".format(my_list[i]))
                
                
                

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)

