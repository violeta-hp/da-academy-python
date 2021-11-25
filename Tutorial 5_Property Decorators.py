#Python OOP 6 - Property Decorators - https://youtu.be/jCzT9XFZ5bw
#Double underscores are called dunder
class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self): #anytime we run this or str fix our problems, ambiguous representation of the object and is used for debugging and log in, etc.
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay) #we recreate the object

    def __str__(self): #str is to display it to the end user
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay     

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(len(emp_1)) #this will print out the num of characters of the employee 1 bcs of the __len__ method

#print(emp_1 + emp_2) #this works with the add method because it takes the self as an employee and other as an another employee


#print (repr(emp_1)) #allow us to change how the objects are printed and displayed
#print (str(emp_1))

#print(emp_1.__repr__()) #Give us the same as above
#print(emp_1.__str__())

# print(emp_1 + emp_2)

#print(len(emp_1))

#ADD
#print(1+2)
#print(int.__add__(1,2)) #this give us the same result as above
#print(str.__add__('a','b'))
