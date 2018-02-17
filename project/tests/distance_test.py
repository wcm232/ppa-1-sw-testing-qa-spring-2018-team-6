import sys
sys.path.append("..")
import unittest
import distance_calc


class TestDistanceMethods(unittest.TestCase):

      def test_true(self):

            # This is a test to ensure that the unit test framework is functioning
            self.assertTrue(True)

      def test_input_accuracy(self):

            # These tests ensure that accurate distances are given for a variety of input types

            # The assumption was made that distances are returned to the nearest thousandth
            
            self.assertEqual(distance_calc.calc(0,0,0,0), 0, msg = "Should return a float")
            self.assertEqual(distance_calc.calc(1,1,1,1), 0, msg = "Should return accurate distance (no difference between points)")
            self.assertEqual(distance_calc.calc(0,0,0,1), 1, msg = "Should return accurate distance (1 point of difference)")
            self.assertEqual(distance_calc.calc(.8,.6,.3,8), 7.417, msg = "Should return accurate distance (floating point numbers)")
            self.assertEqual(distance_calc.calc(.8,-.6,.3,8), 8.615, msg = "Should return accurate distance (negative numbers)")
            self.assertEqual(distance_calc.calc(a=0,b=0,c=0,d=0), 0, msg = "Should return accurate distance (variables as input)")

      def test_input_types(self):

            # These tests ensure that False is returned whenever the function is called with invalid argument types in any of its parameters
            # While not comprehensive, these tests should ensure bad inputs don't get through

            # String test
            self.assertFalse(distance_calc.calc("1",0,0,0))

            # Array test
            self.assertFalse(distance_calc.calc(0,[2],0,0))

            # Dictionary test
            self.assertFalse(distance_calc.calc(0,0,{6,5},0))
      
            # Complex test
            self.assertFalse(distance_calc.calc(0,0,0,3+1j))

            # Tuple test
            self.assertFalse(distance_calc.calc((8, 7),0,0,0))

            # Boole test
            self.assertFalse(distance_calc.calc(True,0,0,0))
            

if __name__ == "__main__":
	from startBuildRunner import *
	unittest.main(testRunner=getUnitTestRunner())
