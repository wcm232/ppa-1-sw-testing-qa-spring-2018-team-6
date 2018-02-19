def errorMsg():
    return "ERROR: Invalid Input"

def tooManyInches(inches):
    if(inches > 12):
        return True
    else:
        return False

def notEnoughInches(inches):
    if(inches < 0):
        return True
    else:
        return False
    
def tooLight(weight):
    if(weight <= 0.03125):
        return True
    else:
        return False

def tooHeavy(weight):
    if(weight >= 1950):
        return True
    else:
        return False

def tooShort(feet, inches):
    if(feet*12+inches <= 10):
        return True
    else:
        return False

def tooTall(feet, inches):
    if(feet*12+inches >= 214):
        return True
    else:
        return False

def checkForRangeErrors(feet, inches, weight):
    if(tooTall(feet, inches)):
        return True
    elif(tooShort(feet, inches)):
        return True
    elif(tooHeavy(weight)):
        return True
    elif(tooLight(weight)):
        return True
    elif(notEnoughInches(inches)):
        return True
    elif(tooManyInches(inches)):
        return True
    else:
        return False

def checkForTypeErrors(feet, inches, weight):
    if(type(feet) is int and type(inches) is int and (type(weight) is int or type(weight) is float)):
        return False
    else:
        return True

def checkForErrors(feet, inches, weight):
    if(checkForTypeErrors(feet, inches, weight)):
        return True
    elif(checkForRangeErrors(feet, inches, weight)):
        return True
    else:
        return False
    
def calcBmi(feet, inches, weight):
    error = checkForErrors(feet, inches, weight)
    if(error == True):
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
