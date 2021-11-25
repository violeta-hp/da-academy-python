#INSTANCES AND CLASS VARIABLES https://www.youtube.com/watch?v=BJ-VvGyQxho
'''class variables are shared among all instances of a classs while instance variables can be unique for each instance
like our names and email and pay, class variables should be the same for each instance'''
class Employee:
    num_of_emps= 0
    raise_amount = 1.04 #this is an attribute
    
    def __init__(self, first, last, pay):
        self.first = first #el .first puede ser cambiado por cualquier cosa
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
        Employee.num_of_emps += 1
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self): #so this is a new method
        self.pay = int(self.pay * Employee.raise_amount) #self, also works and would be better because it can take the value of a subclass. We need to call the % from a class or from an instance, never directly, such in the case of raise_amount alone representing the var 
        
    
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(Employee.num_of_emps)

#print(Employee.__dict__) #raise_amount is part of the class, so that's why the instance sees it and shows 
#print(emp_1.__dict__) #there is no raise_amount in here 

"""Employee.raise_amount = 1.05"""
#emp_1.raise_amount = 1.05 #this will allow that print(emp_1.raise_amount) prints its value because it is not part of the class
'''When we access raise_amount, since they don't have that attribute by themselves, they are accessing the class raise_amount attribute
print(Employee.raise_amount) 
print(emp_1.raise_amount)
print(emp_2.raise_amount) '''


'''print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

emp_1.raise_amount #here we are calling the method
Employee.raise_amount #here we are calling the class'''
