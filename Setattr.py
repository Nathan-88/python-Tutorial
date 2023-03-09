"""
The setattr() function assigns the specified value argument to the specified attribute name (existing or new) of the specified object. This is the counterpart of getattr() method.
Syntax:
setattr(object, name, value)

The setattr() method is equivalent to object.attribute = value
"""


class MyClass:
    pass


obj = MyClass()

# Set an integer attribute
setattr(obj, 'my_int', 42)
print(type(obj.my_int))  # Output: <class 'int'>

# Set a string attribute
setattr(obj, 'my_str', 'Hello, world!')
print(type(obj.my_str))  # Output: <class 'str'>

# Set a list attribute
setattr(obj, 'my_list', [1, 2, 3])
print(type(obj.my_list))  # Output: <class 'list'>

# Set a dictionary attribute
setattr(obj, 'my_dict', {'foo': 'bar', 'baz': 'qux'})
print(type(obj.my_dict))  # Output: <class 'dict'>


"""
When you use setattr to set an attribute on a class object, the attribute will be a class attribute, not an instance attribute.

A class attribute is a variable that belongs to the class itself, rather than to any particular instance of the class. This means that all instances of the class share the same value for that attribute.

Here's an example code snippet to illustrate this:
"""


class MyClass:
    class_attr = 'class attribute'


obj1 = MyClass()
obj2 = MyClass()
# Access the class attribute from both instances
print(obj1.class_attr)  # Output: 'class attribute'
print(obj2.class_attr)  # Output: 'class attribute'

# Set the value of the class attribute using setattr
setattr(MyClass, 'class_attr', 'new value')

# Access the class attribute from both instances again
print(obj1.class_attr)  # Output: 'new value'
print(obj2.class_attr)  # Output: 'new value'