import unittest
from fractions import Fraction
from my_sum import sum

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)
        
    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)
        
if __name__ == '__main__':
    unittest.main()
    
#Test results are the outcomes of the tests that check 
#if the outcome of the program or a unit in the program and 
#the expected result from the program or the unit in the program are equal.
#If test results have failures, I will need to check the program manually before running the test again.
#Otherwise, the program or the unit in the program runs successfully. 
