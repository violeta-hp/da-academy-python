#In here we have 3 different tests https://www.youtube.com/watch?v=6tNS--WetLI
#This script includes 3 tests
import unittest
from Tutorial_7_Employee import Employee

class TestEmployee(unittest.TestCase):
    
    def setUp(self): #These two methods: setup and teardown allow us to have multiple scenarios not just those that are mentioned down below, this because we might have changes in the code to be tested and then we should change all of our code for the tests
        self.emp_1 = Employee('Corey', 'Schafer', 50000)
        self.emp_2 = Employee('Sue', 'Smith', 60000)
    
    def tearDown(self):
        pass

    def test_email(self): #To check if we are getting the expected values
        self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'John.Schafer@email.com') #Make sure that everything works properly
        self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')

    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp_2.fullname, 'Sue Smith')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Schafer') #Checking if the full name changed correctly
        self.assertEqual(self.emp_2.fullname, 'Jane Smith')

    def test_apply_raise(self):
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500) #The pay was raised by 5%
        self.assertEqual(self.emp_2.pay, 63000)


if __name__ == '__main__':
    unittest.main()
