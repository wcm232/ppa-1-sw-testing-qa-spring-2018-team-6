import unittest

def retirement(age, salary, saved, goal):
    saved = saved / 100
    savedAmount = salary * saved
    total = savedAmount
    if total >= goal:
        return True;
    while (100-age) > 0:
        age += 1
    return False;

if __name__ == '__main__':
    unittest.main()

#The main function of the program
#print("Welcome to retirement plan calculator!")
#print("Please enter you current age, annual salary, how much you save per year, and your desired retirement savings goal.")
#age = input("Current Age: ")
#salary = input("Annual Salary: ")
#saved = float(input("Save Percentage(enter without a percent sign): "))
#goal = input("Retirement Goal: ")
#retirement(age, salary, saved, goal)
#print("Thank you for your service!")
