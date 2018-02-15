import unittest
from retirement import retirement

class retirementTesting(unittest.TestCase):
    def test_age_counter(self):
        self.assertFalse(retirement(99, 10, 10, 10))

    def test_goal_reach(self):
        self.assertTrue(retirement(10, 100000, 10, 5000))

if __name__ == '__main__':
    unittest.main()
