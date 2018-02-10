import unittest
try:	
	from teamcity import is_running_under_teamcity
	from teamcity.unittestpy import TeamcityTestRunner
	teamcityRunnerAvailable = True
except:
	teamcityRunnerAvailable = False
	print("teamcity-messages not installed")

def getUnitTestRunner():
	if teamcityRunnerAvailable and is_running_under_teamcity():
		# Use the TeamCity test runner if possible
		print("Using TeamCity test runner")
		return TeamcityTestRunner()  
	else:
		# Otherwise, use the default
		print("Using default test runner")
		return unittest.TextTestRunner()