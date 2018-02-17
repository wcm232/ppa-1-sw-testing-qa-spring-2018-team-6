import emailVerifier
import distance_calc

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
    
    
menu = {
3: distance,
4: email,
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
