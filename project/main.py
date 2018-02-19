import emailVerifier
import distance_calc
import retirement
import tip_calc
import bmi

exitRequested = False

# To add new menu items:
# 1. Create a function here with the desired functionality
# 2. Make sure that function has a docstring. That will be displayed in the menu.abs
# 3. Add an entry in the menu dictionary with the desired number and function reference. Do not invoke the function in the menu.

def requestExit():
    """Exit the application"""
    global exitRequested
    exitRequested = True
    print("Exiting...")
    print("")

def bmiCalculator():
    """Calculate a body mass index given height and weight"""
    feet = input("Enter Height (whole feet value only): ")
    inches = input("Enter Inches Above Highest Foot: ")
    weight = input("Enter Weight (lbs): ")
    try:
        feet = int(feet)
        inches = int(inches)
        weight = float(weight)
        print(bmi.calcBmi(feet, inches, weight))
    except ValueError:
        print("ERROR: Invalid Input")

def email():
    """Verify an email address"""
    email = input("Please enter the email address you wish to verify: ")
    if emailVerifier.verifyEmail(email):
        print("Email address is valid!")
    else:
        print("Email address is not valid :(")
    print("")

def distance():
    """Return the shortest distance between two points"""

    distance_sentinel = 0
    semantics_dictionary = {0: "x1", 1: "y1", 2: "x2", 3: "y2"}
    coordinate_array = []
    good_input = True

    while(distance_sentinel <= 3):
        good_input = True
        print("Coordinate values (x1, y1) (x2, y2)")
        distance_user_input = input("Please input value for data point " + semantics_dictionary[distance_sentinel] + ": ")

        # Error-handling for invalid inputs, increment only when input can be a float
        try:
            distance_user_input = float(distance_user_input)
        except:
            good_input = False

        if good_input == False:
            print("Invalid value, please try again")
        else:
            distance_user_input = float(distance_user_input)
            distance_sentinel += 1
            coordinate_array.append(distance_user_input)


    distance = distance_calc.calculateDistance(coordinate_array[0],
                                               coordinate_array[1],
                                               coordinate_array[2],
                                               coordinate_array[3])
    
    #Tell the user the results of the calculation
    if distance == False and distance != 0:
        print("One or more of the coordinates provided is invalid.")
    else:
        print("The distance between the two coordinates is: " + "{0:.3f}".format(distance) + " units.")
    print()

def retire():
    """Determine retirement savings and goal"""

    ageString = input("Please enter your age: ")
    while not ageString.isnumeric():
        print("Please enter your age as an integer")
        ageString = input("Enter an integer: ")
    age = int(ageString)

    salaryString = input("Please enter your salary: ")
    while not salaryString.isnumeric():
        print("Please enter your salary as an integer")
        ageString = input("Enter an integer: ")
    salary = float(salaryString)

    savedString = input("Please enter how much you wish to save annually (Ex: 35 = 35%): ")
    while not savedString.isnumeric():
        print("Please enter your annual saving rate as an integer")
        savedString = input("Enter an integer: ")
    saved = float(savedString)

    goalString = input("Please enter your goal: ")
    while not goalString.isnumeric():
        print("Please enter your goal as an integer")
        goalString = input("Enter an integer: ")
    goal = int(goalString)

    result = retirement.findRetirementAge(age, salary, saved, goal)
    if result >= 100:
        print("Sorry, your savings goal will not be met.")
    else:
         print("Your savings goal will be met at: ", result)

def tip():
    "Split a tip"
    subtotalString = input("Please enter your sub-total: ")
    while not subtotalString.isnumeric():
        print("Please enter your subtotal as a decimal number")
        subtotalString = input("Enter a decimal number: ")
    subtotal = float(subtotalString)

    partySizeString = input("Please enter the number of people that are paying: ")
    while not partySizeString.isnumeric():
        print("Please the number of people that are paying as an integer")
        partySizeString = input("Enter an integer: ")
    partySize = int(partySizeString)

    dues = tip_calc.calculateTip(subtotal, partySize)

    for i in range(0, len(dues)):
        print("Guest " + str(i+1) + " must pay $" + str(round(dues[i], 2)))

menu = {
1: bmiCalculator,
2: retire,
3: distance,
4: email,
5: tip,
0: requestExit

}

def displayMenu():
    for functionNumber, function in menu.items():
        print(str(functionNumber) + ": " + function.__doc__)

def getMenuItemNumber():
    option = input("Please choose a menu option, then press enter: ")

    while not option.isnumeric():
        print("Invalid input. Please make sure you type a number.")
        print("")
        displayMenu()
        option = input("Please choose a menu option, then press enter: ")

    return int(option)

def main():
    while not exitRequested:
        displayMenu()
        
        optionNumber = getMenuItemNumber()
        while optionNumber not in menu:
            print("Invalid menu option.")
            print("")
            displayMenu()
            optionNumber = getMenuItemNumber()
        
        optionFunction = menu[optionNumber]
        optionFunction()

main()
