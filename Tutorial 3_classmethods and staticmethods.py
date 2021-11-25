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
    
    
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

new_emp_1 = Employee.from_string(emp_str_3)

print(new_emp_1.email)
print(new_emp_1.pay)

#STATIC METHODS
#Don't pass an instance or a class, 



