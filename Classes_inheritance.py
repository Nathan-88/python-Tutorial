class Employer:
    raiseamount = 1.05

    def __init__(self, pay, Fname, Sname):
        self.pay = pay
        self.Fname = Fname
        self.Sname = Sname
        self.email = Fname + Sname + "@email.com"

    def fullname(self):
        return self.Fname + " " + self.Sname

    def Amt(self):
        self.pay = self.pay * Employer.raiseamount


class dev(Employer):
    """this inherits the attributes in class Employer"""

    def __init__(self, pay, Fname, Sname, prog):
        # the super() copies only the pay,Fname and Sname attributes from the parent init method
        super().__init__(pay, Fname, Sname)
        self.prog = prog

    def __repr__(self):
        return "dev({}, {}, {}, {})".format(self.pay, self.Fname, self.Sname, self.prog)


emp_1 = Employer(7000, "Ebuka", "Onwuka")
emp_2 = dev(7000, "Ebuka", "Onwuka", "Python")
print(emp_1.__dict__)
print(repr(emp_2))
print(emp_2.prog)

"""
Use cases for inheritance:

Modeling real-world relationships: Inheritance is useful for modeling real-world relationships between objects. For example, a Dog is a type of Animal, and we can use inheritance to reflect that relationship in our code.

Reusing code: Inheritance allows us to reuse code from the superclass in the subclass, making our code more efficient and maintainable.

Overriding methods: Inheritance allows us to override methods in the superclass in the subclass, which is useful when we want to change the behavior of a method for a specific subclass.

Polymorphism: Inheritance allows us to use polymorphism, which is the ability of a subclass to be treated as an instance of its superclass. This makes it easier to write generic code that can work with objects of different classes.

Inheritance is a powerful tool in Object Oriented Programming, and it's widely used in Python. When used correctly, it can make your code more organized, efficient, and maintainable.
"""