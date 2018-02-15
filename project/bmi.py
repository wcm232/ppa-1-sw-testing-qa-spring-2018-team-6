def calcBmi(feet, inches, weight):
    heightInches = (feet * 12) + inches
    return float(weight)/float(heightInches)/float(heightInches)*703
