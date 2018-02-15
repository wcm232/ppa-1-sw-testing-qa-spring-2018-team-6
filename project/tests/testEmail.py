import unittest
from .. import emailVerifier

# Test classes must inherit from unittest.TestCase
class EmailTests(unittest.TestCase):
	def test_true_with_one_at_sign(self):
		self.assertTrue(email.verifyEmail("test@example.com"))
	
	def test_false_with_zero_at_signs(self):
		self.assertTrue(email.verifyEmail("example.com"))
	
	def test_false_with_more_than_one_at_sign(self):
		self.assertTrue(email.verifyEmail("test@@example.com"))

# Run the tests
if __name__ == "__main__":
	from startBuildRunner import *
	unittest.main(testRunner=getUnitTestRunner())