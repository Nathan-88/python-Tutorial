# class GenericClass():
#     pass

# obj1 = GenericClass()
"""
Using dot notation is equivalent to using the setattr() method.

However, when using dot notation, you might get linting warnings for defining attributes outside of the __init__() method.
"""
# obj1.salary = 100
# obj1.age = 30

# print(getattr(obj1, 'salary'))  # 👉️ 100
# print(getattr(obj1, 'age'))  # 👉️ 30
# print(obj1.salary)  # 👉️ 100
# print(obj1.age)  # 👉️ 30


# class GenericClass():
#     pass

# my_dict = {'name': 'bobbyhadz', 'age': 30}

# obj1 = GenericClass()
# """
# We use a for loop to iterate over a dictionary's items and add the key-value pairs as attributes to the object.
# """
# for key, value in my_dict.items():
#     setattr(obj1, key, value)

# print(getattr(obj1, 'name'))  # 👉️ bobbyhadz
# print(getattr(obj1, 'age'))  # 👉️ 30
# print(obj1.name)


# """
# If you have to use the setattr method from within a class method, you would pass self as the first argument.
# """
# class GenericClass():
#     def __init__(self, dictionary):
#         for key, value in dictionary.items():
#             setattr(self, key, value)

# my_dict = {'name': 'bobbyhadz', 'age': 30}

# obj1 = GenericClass(my_dict)

# print(getattr(obj1, 'name'))  # 👉️ bobbyhadz
# print(getattr(obj1, 'age'))  # 👉️ 30

"""
Add attributes to an Object using SimpleNamespace() 
Use the SimpleNamespace class to create an object.
Use the setattr() function to add attributes to the object.
"""
# from types import SimpleNamespace

# obj1 = SimpleNamespace()

# setattr(obj1, 'salary', 100)
# setattr(obj1, 'language', 'Python')

# print(getattr(obj1, 'salary'))  # 👉️ 100
# print(getattr(obj1, 'language'))  # 👉️ Python

# print(obj1)  # 👉️ namespace(salary=100, language='Python')

"""We can't add attributes to instances of the built-in object class, however, we can add attributes to instances of the SimpleNamespace class.
"""
from types import SimpleNamespace

obj1 = SimpleNamespace(name='bobby', age=30)

setattr(obj1, 'salary', 100)
setattr(obj1, 'language', 'Python')

print(getattr(obj1, 'salary'))  # 👉️ 100
print(getattr(obj1, 'language'))  # 👉️ Python

print(getattr(obj1, 'name'))  # 👉️ bobby
print(getattr(obj1, 'age'))  # 👉️ 30

# 👇️ namespace(name='bobby', age=30, salary=100, language='Python')
print(obj1)
