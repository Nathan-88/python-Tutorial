"""
Create a list of booleans
    # If the number is divisible by 2, the boolean is True
    # If the number is not divisible by 2, the boolean is False
    # List comprehension
"""
# def divisible_by_2(my_list: List[int]) -> List[bool]:
#     return [i % 2 == 0 for i in my_list]

def divisible_by_2(my_list=[]):
    return [True if i % 2 == 0 else False for i in my_list]

my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)

for i in range(len(list_result)):
    print("{:d} {:s} divisible by 2".format(
        my_list[i], "is" if list_result[i] else "is not"))