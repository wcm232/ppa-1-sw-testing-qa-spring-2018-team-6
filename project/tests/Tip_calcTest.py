import sys
import unittest
sys.path.append("..")
import tip_calc
import math

class TestTip(unittest.TestCase):
      def test_evenTip(self):
            temp = [57.5, 57.5]
            self.assertSequenceEqual(tip_calc.tip_calc(100,2), temp)
      def test_unevenTip(self):
            temp = [38.33, 38.33, 38.34]
            self.assertSequenceEqual(tip_calc.tip_calc(100,4), temp)
      
            

if __name__ == "__main__":
	from startBuildRunner import *
	unittest.main(testRunner=getUnitTestRunner())
