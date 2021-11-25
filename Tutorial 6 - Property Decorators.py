#Python OOP 6 - Property Decorators - https://youtu.be/jCzT9XFZ5bw

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property #we can access the email method from the print(emp_1.email) like an attribute
    def email(self): #this is similar to the fullname method
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name): 
        first, last = name.split(' ') #set the first and last name
        self.first = first #setting both values
        self.last = last
    
    @fullname.deleter #If we want to delete the info from an employee
    def fullname(self):
        print('Delete Name!') 
        self.first = None
        self.last = None


emp_1 = Employee('John', 'Smith')
emp_1.fullname = "Corey Schafer"

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname) #this calls the method fullname

del emp_1.fullname