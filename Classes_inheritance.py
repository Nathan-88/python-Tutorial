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
