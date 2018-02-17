import unittest
import distance_calc


class TestDistanceMethods(unittest.TestCase):

      # The assumption was made that distances are returned to the nearest thousandth
            
      def test_input_base(self):
            self.assertEqual(distance_calc.calculateDistance(0,0,0,0), 0)

      def test_input_accuracy_equivalent(self):
            self.assertEqual(distance_calc.calculateDistance(1,1,1,1), 0)

      def test_input_accuracy_difference(self):
            self.assertEqual(distance_calc.calculateDistance(0,0,0,1), 1)

      def test_input_accuracy_floats(self):
            self.assertEqual(distance_calc.calculateDistance(.8,.6,.3,8), 7.417)

      def test_input_accuracy_negatives(self):
            self.assertEqual(distance_calc.calculateDistance(.8,-.6,.3,8), 8.615)

      def test_input_accuracy_variables(self):
            a=.8
            b=.6
            c=.3
            d=8
            self.assertEqual(distance_calc.calculateDistance(a,b,c,d), 7.417)

      def test_input_string(self):
            # String test
            self.assertFalse(distance_calc.calculateDistance("1",0,0,0))

      def test_input_array(self):
            # Array test
            self.assertFalse(distance_calc.calculateDistance(0,[2],0,0))

      def test_input_dictionary(self):
            # Dictionary test
            self.assertFalse(distance_calc.calculateDistance(0,0,{6,5},0))

      def test_input_complex(self):      
            # Complex test
            self.assertFalse(distance_calc.calculateDistance(0,0,0,3+1j))

      def test_input_tuple(self):
            # Tuple test
            self.assertFalse(distance_calc.calculateDistance((8, 7),0,0,0))

      def test_input_boole(self):
            # Boole test
            self.assertFalse(distance_calc.calculateDistance(True,0,0,0))
