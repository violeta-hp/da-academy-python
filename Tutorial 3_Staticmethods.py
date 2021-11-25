#STATIC METHODS
#Don't pass an instance or a class
#Tutorial 3 continuation...
#INSTANCES AND CLASS VARIABLES https://www.youtube.com/watch?v=rq8cL2XMM5M
'''About the differences between regular methods, class methods and static methods.
Regular and class methods take the instance as the first argument, and it is called self'''
class Employee:
    num_of_emps= 0
    raise_amt = 1.04 #this is an attribute
    
    def __init__(self, first, last, pay):
        self.first = first #el .first puede ser cambiado por cualquier cosa
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
        Employee.num_of_emps += 1
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self): 
        self.pay = int(self.pay * self.raise_amount) 
        
    #HOW TO CONVERT A REGULAR METHOD INTO A CLASS METHOD, WE ADD @CLASSMETHOD WHICH IS A DECORATOR
    @classmethod #Class Methods are alternative to constructors
    def set_raise_amt(cls, amount): #here we are working with the class instead of the instance
        cls.raise_amt = amount
        
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-') #parsing the string
        return cls(first, last, pay)  #this will receive the employee object
    
    @staticmethod #if the day is within the week
    def is_workday(day): 
        if day.weekday() == 5 or day.weekday() == 6: #5 is saturday and 6 is sunday, 0 is monday and so on till sunday 6
            return False
        return True

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

import datetime
my_date = datetime.date(2016, 7, 4) #4 is friday 

print(Employee.is_workday(my_date))

