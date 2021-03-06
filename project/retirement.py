def findRetirementAge(age, salary, saved, goal):
    if type(age) is not int:
        return False
    if type(salary) is not float:
        return False
    if type(saved) is not float:
        return False
    if type(goal) is not int:
        return False
    if age < 16:
        return False
    if age >= 100:
        return False
    if salary < 0:
        return False
    if saved < 0:
        return False
    if saved > 100:
        return False
    if goal < 0:
        return False
    saved = saved / 100
    savedAmount = salary * saved
    total = savedAmount
    currentAge = age
    while (100-currentAge) > 0:
        employerMatch = total + (total * 0.35)
        if employerMatch >= goal:
           return currentAge
        total += savedAmount
        currentAge += 1
    return currentAge
