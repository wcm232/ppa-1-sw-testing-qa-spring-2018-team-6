import fixModuleDiscovery
import unittest
import emailVerifier

# Test classes must inherit from unittest.TestCase
class EmailTests(unittest.TestCase):

	# Input must be a string
	# Aka. ensure non-strings are rejected. All other tests will tests that test for True also test for allowing strings.
	def test_reject_null(self):
		self.assertFalse(emailVerifier.verifyEmail(None))

	def test_reject_bad_types(self):	
		# This test isn't 100% comprehensive, but should give reasonable indication of whether non-String types are accepted
		for badInput in [10, True, 7.5, EmailTests()]:
			self.assertFalse(emailVerifier.verifyEmail(badInput), msg="Incorrectly accepted " + str(badInput))

	# Can contain one and only one @ sign
	def test_accept_one_at_sign(self):
		self.assertTrue(emailVerifier.verifyEmail("test@example.com"))
	
	def test_reject_zero_at_signs(self):
		self.assertFalse(emailVerifier.verifyEmail("example.com"))
	
	def test_reject_more_than_one_at_sign(self):
		self.assertFalse(emailVerifier.verifyEmail("test@@example.com"))

	# Right of @ must follow domain rules
	# Only basic rules will be tested, as the assignment does not list the requirements, and domain names can contain a wide range of characters. Even emoji.
	# The exact rules even vary by TLD
	# So we're only going to test to make sure the basics work

	def test_reject_without_domain(self):
		self.assertFalse(emailVerifier.verifyEmail("test@"))
	
	def test_accept_standard_domain_name(self):
		self.assertTrue(emailVerifier.verifyEmail("test@example.com"))

	def test_accept_subdomain_name(self):
		self.assertTrue(emailVerifier.verifyEmail("test@my.example.com"))

	def test_accept_localhost_domain_name(self):
		self.assertTrue(emailVerifier.verifyEmail("test@localhost"))

	def test_accept_ip_domain_name(self):
		self.assertTrue(emailVerifier.verifyEmail("test@127.0.0.1"))

	# Left of @ can contain text
	# The requirements are vague, so let's assume letters and numbers are valid unless otherwise indicated

	def test_reject_without_username(self):
		self.assertFalse(emailVerifier.verifyEmail("@example.com"))

	def test_allow_letters(self):
		self.assertTrue(emailVerifier.verifyEmail("abcdefghijklmnopqrstuvwxyz@example.com"))

	def test_allow_numbers(self):
		self.assertTrue(emailVerifier.verifyEmail("test0123456789@example.com"))

	# Left of @ can contain periods

	def test_allow_periods(self):
		self.assertTrue(emailVerifier.verifyEmail("test.test@example.com"))

	# Left of @ cannot have consecutive periods

	def test_reject_two_consecutive_periods(self):
		self.assertFalse(emailVerifier.verifyEmail("test..test@example.com"))

	# Left of @ cannot start or end with periods

	def test_reject_username_starting_with_period(self):
		self.assertFalse(emailVerifier.verifyEmail(".test@example.com"))

	def test_reject_username_ending_with_period(self):
		self.assertFalse(emailVerifier.verifyEmail("test.@example.com"))

	# Left of @ cannot start with non-numeric character

	def test_reject_starting_with_zero(self):
		self.assertFalse(emailVerifier.verifyEmail("0test@example.com"))

	def test_reject_starting_with_zero(self):
		self.assertFalse(emailVerifier.verifyEmail("1test@example.com"))

	def test_reject_starting_with_zero(self):
		self.assertFalse(emailVerifier.verifyEmail("2test@example.com"))

	def test_reject_starting_with_zero(self):
		self.assertFalse(emailVerifier.verifyEmail("3test@example.com"))

	def test_reject_starting_with_zero(self):
		self.assertFalse(emailVerifier.verifyEmail("4test@example.com"))

	def test_reject_starting_with_zero(self):
		self.assertFalse(emailVerifier.verifyEmail("5test@example.com"))

	def test_reject_starting_with_zero(self):
		self.assertFalse(emailVerifier.verifyEmail("6test@example.com"))

	def test_reject_starting_with_zero(self):
		self.assertFalse(emailVerifier.verifyEmail("7test@example.com"))

	def test_reject_starting_with_zero(self):
		self.assertFalse(emailVerifier.verifyEmail("8test@example.com"))

	def test_reject_starting_with_zero(self):
		self.assertFalse(emailVerifier.verifyEmail("9test@example.com"))

	# Left of @ can contain !$%*+-=?^_{|}~

	def test_can_contain_exclamation(self):
		self.assertTrue(emailVerifier.verifyEmail("test!test@example.com"))

	def test_can_contain_dollar(self):
		self.assertTrue(emailVerifier.verifyEmail("test$test@example.com"))

	def test_can_contain_percent(self):
		self.assertTrue(emailVerifier.verifyEmail("test%test@example.com"))

	def test_can_contain_asterisk(self):
		self.assertTrue(emailVerifier.verifyEmail("test*test@example.com"))

	def test_can_contain_plus(self):
		self.assertTrue(emailVerifier.verifyEmail("test+test@example.com"))

	def test_can_contain_minus(self):
		self.assertTrue(emailVerifier.verifyEmail("test-test@example.com"))

	def test_can_contain_equals(self):
		self.assertTrue(emailVerifier.verifyEmail("test=test@example.com"))

	def test_can_contain_question(self):
		self.assertTrue(emailVerifier.verifyEmail("test?test@example.com"))

	def test_can_contain_carot(self):
		self.assertTrue(emailVerifier.verifyEmail("test^test@example.com"))

	def test_can_contain_underscore(self):
		self.assertTrue(emailVerifier.verifyEmail("test_test@example.com"))

	def test_can_contain_open_curly_brace(self):
		self.assertTrue(emailVerifier.verifyEmail("""test!test@example.com"""))

	def test_can_contain_pipe(self):
		self.assertTrue(emailVerifier.verifyEmail("test|test@example.com"))

	def test_can_contain_close_curly_brace(self):
		self.assertTrue(emailVerifier.verifyEmail("test}test@example.com"))

	def test_can_contain_tilde(self):
		self.assertTrue(emailVerifier.verifyEmail("test~test@example.com"))

	# Left of @ cannot contain “ # ‘ /\`

	def test_cannot_contain_double_quote(self):
		self.assertFalse(emailVerifier.verifyEmail("test\"test@example.com"))

	# - Not sure if this requirement was intended, but IIRC this is a requirement for standard email addresses
	def test_cannot_contain_space(self):
		self.assertFalse(emailVerifier.verifyEmail("test test@example.com"))

	def test_cannot_contain_pound(self):
		self.assertFalse(emailVerifier.verifyEmail("test#test@example.com"))

	def test_cannot_contain_single_quote(self):
		self.assertFalse(emailVerifier.verifyEmail("""test'test@example.com"""))

	def test_cannot_contain_forward_slash(self):
		self.assertFalse(emailVerifier.verifyEmail("""test/test@example.com"""))

	def test_cannot_contain_back_slash(self):
		self.assertFalse(emailVerifier.verifyEmail("""test\test@example.com"""))

	def test_cannot_contain_back_tick(self):
		self.assertFalse(emailVerifier.verifyEmail("test`test@example.com"))


# Run the tests
if __name__ == "__main__":
	import startBuildRunner
	unittest.main(testRunner=startBuildRunner.getUnitTestRunner())