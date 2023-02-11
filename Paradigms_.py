# def fact(n):
#     fac = 1
#     for i in range(1,n+1):
#         fac *= i
#     return fac
    
# n = 6
# print(fact(6))
# print(dir(list))
class MyList(list):
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        print(sorted(self))

my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)
print(my_list)
my_list.print_sorted()
print(my_list)
