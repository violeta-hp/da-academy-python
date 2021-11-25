import unittest 
import Tutorial_7_Calc

class TestCalc(unittest.TestCase): #will give us capability for using the TestCase
    
    def add_test(self):
        self.assertEqual(Tutorial_7_Calc.add(10,5), 15)
        self.assertEqual(Tutorial_7_Calc.add(-1,1), 0)
        self.assertEqual(Tutorial_7_Calc.add(-1,-1), -2)
        
    def subtract_test(self):
        self.assertEqual(Tutorial_7_Calc.substract(10,5), 5)
        self.assertEqual(Tutorial_7_Calc.substract(-1,1), -2)
        self.assertEqual(Tutorial_7_Calc.substract(-1,-1), 0)

    def multiply_test(self):
        self.assertEqual(Tutorial_7_Calc.multiply(10,5), 50)
        self.assertEqual(Tutorial_7_Calc.multiply(-1,1), -1)
        self.assertEqual(Tutorial_7_Calc.multiply(-1,-1), 1)

    def divide_test(self):
        self.assertEqual(Tutorial_7_Calc.divide(10,5), 2)
        self.assertEqual(Tutorial_7_Calc.divide(-1,1), -1)
        self.assertEqual(Tutorial_7_Calc.divide(-1,-1), 1)
        self.assertEqual(Tutorial_7_Calc.divide(-1,-1), 1)
        
if __name__ == '__main__': 
    unittest.main()