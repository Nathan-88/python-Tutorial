"""
Here's an example function that serializes a given instance of a class into a dictionary with simple data structures:
"""


def class_to_json(obj):
    json_dict = {}
    for attr_name in dir(obj):
        attr_value = getattr(obj, attr_name)
        if isinstance(attr_value, (list, dict, str, int, bool)):
            json_dict[attr_name] = attr_value
    return json_dict
"""
This function works by using the dir function to get a list of all the attributes of the object, and then checking each attribute to see if it's one of the serializable data types. If it is, the attribute is added to the dictionary that will be returned as the serialized JSON.
"""

# Here's an example usage of this function with a sample class:


class Person:
    def __init__(self, name, age, is_alive):
        self.name = name
        self.age = age
        self.is_alive = is_alive
        self.address = {
            'street': '123 Main St',
            'city': 'Anytown',
            'state': 'CA'
        }
        self.phone_numbers = ['555-1234', '555-5678']


person = Person('Alice', 30, True)
setattr(person, "occupation", "SE")
json_data = class_to_json(person)
print(json_data)
"""
This would output a dictionary containing the serializable attributes of the Person instance:
"""