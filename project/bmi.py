import types

def errorMsg():
    return "ERROR: Invalid Input"

def tooManyInches(inches):
    if(inches > 12):
        return 1
    else:
        return 0

def notEnoughInches(inches):
    if(inches < 0):
        return 1
    else:
        return 0
    
def tooLight(weight):
    if(weight <= 0.03125):
        return 1
    else:
        return 0

def tooHeavy(weight):
    if(weight >= 1950):
        return 1
    else:
        return 0

def tooShort(feet, inches):
    if(feet*12+inches <= 10):
        return 1
    else:
        return 0

def tooTall(feet, inches):
    if(feet*12+inches >= 214):
        return 1
    else:
        return 0

def checkForRangeErrors(feet, inches, weight):
    if(tooTall(feet, inches)):
        return 1
    elif(tooShort(feet, inches)):
        return 1
    elif(tooHeavy(weight)):
        return 1
    elif(tooLight(weight)):
        return 1
    elif(notEnoughInches(inches)):
        return 1
    elif(tooManyInches(inches)):
        return 1
    else:
        return 0

def checkForTypeErrors(feet, inches, weight):
    if((isinstance(feet, types.IntType) and (str(feet) != "True" and str(feet) != "False"))
        and
        (isinstance(inches, types.IntType) and (str(inches) != "True" and str(inches) != "False"))
       and 
        ((isinstance(weight, types.IntType) or isinstance(weight, types.FloatType)) and
         (str(weight) != "True" and str(weight) != "False"))):
        return 0
    else:
        return 1

def checkForErrors(feet, inches, weight):
    if(checkForTypeErrors(feet, inches, weight)):
        return 1
    elif(checkForRangeErrors(feet, inches, weight)):
        return 1
    else:
        return 0
    
def calcBmi(feet, inches, weight):
    error = checkForErrors(feet, inches, weight)
    if(error == 1):
        return errorMsg()
    else:
        heightInches = (feet * 12) + inches
        bmi = float(weight)/float(heightInches)/float(heightInches)*703
        bmi = round(bmi, 1)
        if(bmi > 29.9):
            cat = "Obese"
        elif(bmi > 24.9):
            cat = "Overweight"
        elif(bmi > 18.4):
            cat = "Normal"
        else:
            cat = "Underweight"
        return str(bmi) + " " + cat
