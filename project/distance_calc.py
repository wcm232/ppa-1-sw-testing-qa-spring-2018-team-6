"""
Distance Formula Calculation
============================
Degenerate case: Function returns a float
	Should return True for isFloat(distance(1,2,3,4))
Input should be some combo of four ints and floats
Should return correct values
	Points are the same:
		Should return 0 for (1,1,1,1)
	Points differ:
		Should return 1 for (0,0,0,1)
	Floats:
		Should return 7.417 for (.8,.6,.3,8)
	Negative Numbers:
		Should return 8.615 for (.8,-.6,.3,8)
	Variables:
		Should return 0 for (a,b,c,d) where all variables equal 0
Should return TypeError for any non-ints or non-floats in any field
	("1",0,0,0) (string)
	(0,[2],0,0) (array)
	(0,0,{6,5},0) (dictionary)
	(0,0,0,3+1j) (complex number)
	(5L,0,0,0) (long)
	((8),0,0,0) (tuple)
"""	
      
import unittest
import math

def distance_calc(a,b,c,d):

      if (type(a) is not int or type(a) is not float
      or type(b) is not int or type(b) is not float
      or type(c) is not int or type(c) is not float
      or type(d) is not int or type(d) is not float):
          return TypeError
      else:
            return float(sqrt((a-c)^2+(b-d)^2))


class TestDistanceMethods(unittest.TestCase):

      def test_true(self):
            self.assertTrue(True)

      def test_input_accuracy(self):
            self.assertIs(distance_calc(0,0,0,0), 5.0, "Should return a float")
            self.assertEqual(distance_calc(1,1,1,1), 0, "Should return accurate distance (no difference between points)")
            self.assertEqual(distance_calc(0,0,0,1), 1, "Should return accurate distance (1 point of difference)")
            self.assertEqual(distance_calc(.8,.6,.3,8), 7.417, "Should return accurate distance (floating point numbers)")
            self.assertEqual(distance_calc(.8,-.6,.3,8), 8.615, "Should return accurate distance (negative numbers)")
            self.assertEqual(distance_calc(a=0,b=0,c=0,d=0), 0, "Should return accurate distance (variables as input)")

      def test_input_types(self):
            self.assertRaises(distance_calc("1",0,0,0), TypeError)
            self.assertRaises(distance_calc(0,[2],0,0), TypeError)
            self.assertRaises(distance_calc(0,0,{6,5},0), TypeError)
            self.assertRaises(distance_calc(0,0,0,3+1j), TypeError)
            self.assertRaises(distance_calc(5L,0,0,0), TypeError)
            self.assertRaises(distance_calc((8),0,0,0), TypeError)

if __name__ == "__main__":
	unittest.main()
