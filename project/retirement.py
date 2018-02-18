import unittest

def retirement(age, salary, saved, goal):
    if type(age) is not int:
        print("Your age must be a valid intger type.")
        return False
    if type(salary) is not float:
        print("Your salary must be a valid integer type.")
        return False
    if type(saved) is not float:
        print("The percentage you wish to save every year must be a valid integer.")
        return False
    if type(goal) is not int:
        print("Your goal must be a valid integer type.")
        return False
    if age < 16:
        print("Invalid user age.")
        return False
    if age >= 100:
        print("Invalid user age.")
        return False
    if salary < 0:
        print("Invalid salary")
        return False
    saved = saved / 100
    savedAmount = salary * saved
    total = savedAmount
    while (100-age) > 0:
        total1 = total + (total * 0.35)
        if total1 >= goal:
            print("Savings goal is met at the age of: %d" % age)
            return True
        total += savedAmount
        age += 1
    print("Your savings goal will not be met at the rate you are saving.")
    return False

if __name__ == '__main__':
    unittest.main()
