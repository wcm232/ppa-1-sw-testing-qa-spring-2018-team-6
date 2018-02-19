import fixModuleDiscovery
import unittest
import tip_calc

class TestTip(unittest.TestCase):
      def test_require_number_arg1(self):
            for badInput in ["10", True, TestTip()]:
                  with self.assertRaises(TypeError):                        
                        tip_calc.calculateTip(badInput, 1)
      def test_require_number_arg2(self):
            for badInput in ["10", True, TestTip()]:
                  with self.assertRaises(TypeError):                        
                        tip_calc.calculateTip(1, badInput)
      def test_fail_zero_way_split(self):
            with self.assertRaises(ValueError):                        
                  tip_calc.calculateTip(1, 0)
      def test_fail_negative_way_split(self):
            with self.assertRaises(ValueError):                        
                  tip_calc.calculateTip(1, -1)
      def test_one_way_split(self):
            self.assertEqual([1.15], tip_calc.calculateTip(1, 1))
            self.assertEqual([5.75], tip_calc.calculateTip(5, 1))
      def test_two_way_even_split(self):
            self.assertEqual([0.69, 0.69], tip_calc.calculateTip(1.2, 2))
            self.assertEqual([2.99, 2.99], tip_calc.calculateTip(5.2, 2))
      def test_three_way_uneven_split(self):
            self.assertEqual([0.30, 0.31, 0.31], tip_calc.calculateTip(0.8, 3))
            self.assertEqual([5.82, 5.83, 5.83], tip_calc.calculateTip(15.2, 3))

      def test_five_way_uneven_split(self):            
            self.assertEqual([3.48, 3.47, 3.47, 3.47, 3.47], tip_calc.calculateTip(15.1, 5))
