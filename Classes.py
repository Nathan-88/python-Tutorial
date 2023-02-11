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

    @classmethod
    def frm_str(cls, datm):
        Fname, Sname, pay = datm.split('-')
        return cls(pay, Fname, Sname)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6: #in python sunday is 6 and monday is 0
            return(f"{day} is not a week day")
        else:
             return(f"{day} is a week day")

emp_1 = Employer(7000, "Ebuka", "Onwuka")
print(emp_1.pay)
print(emp_1.__dict__)
emp_1.Amt()
print(emp_1.pay)
print(emp_1.fullname())
emp1 = "john-doe-1000"
name_day = Employer.frm_str(emp1)
print(name_day.email)

import datetime
my_date = datetime.date(2023, 1, 29)
print(Employer.is_workday(my_date))