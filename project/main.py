import emailVerifier

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

menu = {
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
