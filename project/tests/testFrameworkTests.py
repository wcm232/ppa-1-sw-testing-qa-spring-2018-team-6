import unittest

# Test classes must inherit from unittest.TestCase
class TestFrameworkTests(unittest.TestCase):
	# Test names must begin with "test_"
	def test_true(self):
		self.assertTrue(True)
		