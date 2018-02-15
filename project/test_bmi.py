import unittest
import sys
sys.path.append("C:\\Users\\AustinBrown\\qaProject\\ppa-1-sw-testing-qa-spring-2018-team-6\\project")
import bmi

class TestBmi(unittest.TestCase):
    def test_worksWithProperInput(self):
        result = bmi.bmi(5,10,165)
        self.assertEqual(result, 23.672448979591838)

if __name__ == "__main__":
	from startBuildRunner import *
	unittest.main(testRunner=getUnitTestRunner())
