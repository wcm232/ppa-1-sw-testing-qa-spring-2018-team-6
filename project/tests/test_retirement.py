import fixModuleDiscovery
import unittest
from retirement import retirement

class retirementTesting(unittest.TestCase):
    def test_age_string(self):
        self.assertFalse(retirement('30', 100000.0, 35.0, 50000))

    def test_age_float(self):
        self.assertFalse(retirement(30.0, 100000.0, 35.0, 50000))

    def test_age_out_of_range_below(self):
        self.assertFalse(retirement(10, 100000.0,35.0,50000))

    def test_age_out_of_range_above(self):
        self.assertFalse(retirement(101, 100000.0, 35.0, 50000))

    def test_age_edge(self):
        self.assertFalse(retirement(100, 100000.0, 35.0, 100000))

    def test_age_out_of_range(self):
        self.assertFalse(retirement(95, 100000.0, 1.0, 100000))

    def test_salary_int(self):
        self.assertFalse(retirement(30, 100000, 35.0, 50000))

    def test_salary_string(self):
        self.assertFalse(retirement(30, '100000.0', 35.0, 50000))

    def test_salary_below(self):
        self.assertFalse(retirement(30, -3, 35.0, 50000))

    def test_saved_string(self):
        self.assertFalse(retirement(30, 100000.0, '35.0', 50000))

    def test_saved_int(self):
        self.assertFalse(retirement(30, 100000.0, 35, 50000))

    def test_saved_below(self):
        self.assertFalse(retirement(30, 100000.0, -3.0, 50000))

    def test_saved_above(self):
        self.assertFalse(retirement(30, 100000.0, 101.0, 50000))

    def test_goal_string(self):
        self.assertFalse(retirement(30, 100000.0, 35.0, '50000'))

    def test_goal_float(self):
        self.assertFalse(retirement(30, 100000.0, 35.0, 50000.0))

    def test_goal_reach1(self):
        self.assertTrue(retirement(30, 100000.0, 35.0, 50000))

    def test_goal_reach2(self):
        self.assertTrue(retirement(22, 80000.0, 15.0, 1000000))

    def test_goal_below(self):
        self.assertFalse(retirement(30, 100000.0, 35.0, -3))

if __name__ == '__main__':
    unittest.main()
