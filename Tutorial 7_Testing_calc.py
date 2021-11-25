import unittest 
import Tutorial_7_Calc

class TestCalc(unittest.TestCase): #will give us capability for using the TestCase
    
    def tets_add(self):
        self.assertEqual(Tutorial_7_Calc.add(10,5), 15)
        self.assertEqual(Tutorial_7_Calc.add(-1,1), 0)
        self.assertEqual(Tutorial_7_Calc.add(-1,-1), -2)
        
    def test_substract(self):
        self.assertEqual(Tutorial_7_Calc.substract(10,5), 5)
        self.assertEqual(Tutorial_7_Calc.substract(-1,1), -2)
        self.assertEqual(Tutorial_7_Calc.substract(-1,-1), 0)

    def test_multiply(self):
        self.assertEqual(Tutorial_7_Calc.multiply(10,5), 50)
        self.assertEqual(Tutorial_7_Calc.multiply(-1,1), -1)
        self.assertEqual(Tutorial_7_Calc.multiply(-1,-1), 1)

    def test_divide(self):
        self.assertEqual(Tutorial_7_Calc.divide(10,5), 2)
        self.assertEqual(Tutorial_7_Calc.divide(-1,1), -1)
        self.assertEqual(Tutorial_7_Calc.divide(-1,-1), 1)
        #self.assertEqual(Tutorial_7_Calc.divide(-1,-1), 2.5) will give us error if we change the / for // in Tutorial_7_Calc
        
        self.assertRaises(ValueError, Tutorial_7_Calc.divide, 10, 0) #Value error is the exception we expect, the 2nd arg is the function we wanna run and then we passed in each argument that we want to pass into 
                                                                    #the divide function separately. If we don't use this and only run the function it will throw an exception error and our
                                                                    #test will fail
        with self.assertRaises(ValueError):
            Tutorial_7_Calc.divide(10,0)
        
if __name__ == '__main__': 
    unittest.main()