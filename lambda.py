# lambda arguments: expression

# my_list = [1,2,3,4,5]

# num = list(map(lambda x: x**2, my_list))
# print(num)
""" 
map() function: You can use lambda functions with the map() function to apply a function to all elements of an iterable (such as a list). For example, the following code squares each element of a list using a lambda function:
"""
# nums = [1, 2, 3, 4]
# squared_nums = list(map(lambda x: x**2, nums))
# print(squared_nums)

"""
filter() function: You can use lambda functions with the filter() function to filter elements from an iterable based on a certain condition. For example, the following code filters out even numbers from a list using a lambda function:
"""
# nums = [1, 2, 3, 4, 5, 6]
# odd_nums = list(filter(lambda x: x % 2 != 0, nums))
# print (odd_nums)
"""
sorted() function: You can use lambda functions with the sorted() function to specify a custom sorting key. For example, the following code sorts a list of strings by their length using a lambda function:
"""
# words = ['cat', 'dog', 'elephant', 'bird']
# sorted_words = sorted(words, key=lambda x: len(x))
# print(sorted_words)
