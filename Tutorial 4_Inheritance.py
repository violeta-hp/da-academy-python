#Python OOP Tutorial 4: Inheritance - Creating Subclasses https://www.youtube.com/watch?v=RSl87lqOXDE
'''Creating different types of employees, devs and managers and they will be good candidates
for subclasses because they will share attributes, we can reuse the code and inherit it from employee'''

class Employee:
    raise_amt = 1.04 #this is an attribute
    
    def __init__(self, first, last, pay):
        self.first = first 
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self): 
        self.pay = int(self.pay * self.raise_amount) 

class Developer(Employee):   #By adding the employee argument we get all the information from the class employee in the class developer
    raise_amt = 1.10
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay) #this will pass the attributes from the 1st init method 
        #Employee.__init__(self, first, last, pay) also valid 
        self.prog_lang = prog_lang        

class Manager(Employee):
    raise_amt = 1.10
    def __init__(self, first, last, pay, plang):
        Employee.__init__(first, last, pay) #using the above method instead of super
        self.plang = plang

class Managers(Employee):
    def __init__(self, first, last, pay, employees=None): #list of employees
        super().__init__(first, last, pay)
        if employees is None: #if the list of employees is none
            self.employees = []
        else:
            self.employees = employees #a list or dict are mutable that's why he used none

    def add_emp(self, emp): #Add employees to the list
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp): #Remove employees from the list
        if emp in self.employees:
            self.employees.remove(emp)
            
    def print_emps(self): #Print out all the employees from the list
        for emp in self.employees:
            print('--->', emp.fullname())
            
dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

mgr_1 = Managers('Sue', 'Smith', 90000, [dev_1])

#Two built in functions--> instance and subclass
print(isinstance(mgr_1, Managers))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))

print(issubclass(Developer, Employee))
print(issubclass(Manager, Developer))

#print(mgr_1.email)

#mgr_1.add_emp(dev_2)
#mgr_1.print_emps()


#manager_1 = Manager('Violeta','Hernandez', 50300, 'Spanish')
#manager_2 = Manager('Rosa', 'Perez', 40203, 'English')


#print(dev_1.email)
#print(dev_2.prog_lang)

#print(manager_1.email)
#print(manager_2.plang)

#print(dev_1.pay)
#dev_1.apply_raise()
#print(dev_1.pay)

#print(help(Developer))
#print(dev_2.email)    
#print(dev_1.email)



