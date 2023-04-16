"""
The map() function in Python is a built-in function that allows you to apply a function to every element in an iterable, such as a list, tuple, or set. It returns a new iterable containing the results of applying the function to each element in the original iterable.

Here's the syntax for the map() function:

map(function, iterable)
Where:

function: the function to apply to each element in the iterable. This can be a built-in function or a user-defined function.
iterable: the iterable to apply the function to.
Here's an example of using the map() function to apply a function to every element in a list:
"""

"""
def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
squares = map(square, numbers)

print(list(squares))  # [1, 4, 9, 16, 25]

In this example, we define a function square() that takes an argument x and returns x ** 2. We then create a list numbers containing the numbers 1 through 5, and use the map() function to apply the square() function to each element in numbers. The result is a new iterable squares containing the squares of each element in numbers. Finally, we convert squares to a list and print the result.
"""

"""
You can also use lambda functions with map(). For example, let's say you want to convert a list of strings to uppercase:

fruits = ['apple', 'banana', 'cherry']
upper_fruits = map(lambda x: x.upper(), fruits)

print(list(upper_fruits))  # ['APPLE', 'BANANA', 'CHERRY']

In this example, we use a lambda function to apply the upper() method to each element in the fruits list, converting them to uppercase. The result is a new iterable upper_fruits containing the uppercase versions of each element in fruits. Finally, we convert upper_fruits to a list and print the result.
"""