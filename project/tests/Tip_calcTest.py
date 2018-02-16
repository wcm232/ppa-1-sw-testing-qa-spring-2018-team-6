import sys
import unittest
sys.path.append("..")
import tip_calc

class TestTip(unittest.TestCase):
      def test_input_type(self):
            self.assertRaises(TypeError, tip_calc("100",3))
      def test_true_type(self):
            self.assertTrue(tip_calc.tip_calc(100,3))
      
            

if __name__ == "__main__":
	from startBuildRunner import *
	unittest.main(testRunner=getUnitTestRunner())
