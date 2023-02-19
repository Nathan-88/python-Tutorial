"""
Write a class Student that defines a student by: (based on 9-student.py)

Public instance attributes:
first_name
last_name
age
Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
Public method def to_json(self, attrs=None): that retrieves a dictionary representation of a Student instance(same as 8-class_to_json.py):
If attrs is a list of strings, only attribute names contained in this list must be retrieved.
Otherwise, all attributes must be retrieved
You are not allowed to import any module
"""


class Student():
    """defines a class of student
    """

    def __init__(self, first_name, last_name, age):
        """define instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ If attrs is a list of strings, only attribute names
        contained in this list must be retrieved.
        Otherwise, all attributes must be retrieved
        """
        if attrs is None:
            return self.__dict__
        else:
            diction = {}
            if isinstance(attrs, list):
                if all(isinstance(attr, str) for attr in attrs):
                    for i in attrs:
                        if i in self.__dict__:
                            diction.update({i: self.__dict__[i]})
            return diction


student_1 = Student("John", "Doe", 23)
student_2 = Student("Bob", "Dylan", 27)

j_student_1 = student_1.to_json()
j_student_2 = student_2.to_json(['first_name', 'age'])
j_student_3 = student_2.to_json(['middle_name', 'age'])

print(j_student_1)
print(j_student_2)
print(j_student_3)


