import sys
sys.path.append("..")
import unittest
import distance_calc


class TestDistanceMethods(unittest.TestCase):

      def test_true(self):
            self.assertTrue(True)

      def test_input_accuracy(self):
            self.assertEqual(distance_calc.calc(0,0,0,0), 0, "Should return a float")
            self.assertEqual(distance_calc.calc(1,1,1,1), 0, "Should return accurate distance (no difference between points)")
            self.assertEqual(distance_calc.calc(0,0,0,1), 1, "Should return accurate distance (1 point of difference)")
            self.assertEqual(distance_calc.calc(.8,.6,.3,8), 7.417, "Should return accurate distance (floating point numbers)")
            self.assertEqual(distance_calc.calc(.8,-.6,.3,8), 8.615, "Should return accurate distance (negative numbers)")
            self.assertEqual(distance_calc.calc(a=0,b=0,c=0,d=0), 0, "Should return accurate distance (variables as input)")

      def test_input_types(self):
            self.assertRaises(TypeError, distance_calc.calc("1",0,0,0))
            self.assertRaises(TypeError, distance_calc.calc(0,[2],0,0))
            self.assertRaises(TypeError, distance_calc.calc(0,0,{6,5},0))
            self.assertRaises(TypeError, distance_calc.calc(0,0,0,3+1j))
            self.assertRaises(TypeError, distance_calc.calc((8),0,0,0))

if __name__ == "__main__":
	from startBuildRunner import *
	unittest.main(testRunner=getUnitTestRunner())
