import math

def calculateTip(sub_total, num_people):
    if type(sub_total) is not int and type(sub_total) is not float:
        raise TypeError()

    if type(num_people) is not int:
        raise TypeError()

    if num_people < 1:
        raise ValueError()    

    total_bill = round(sub_total * 1.15, 2)
    per_person = total_bill / num_people

    dues = []
    per_person_rounded = round(per_person, 2)   
    unassigned_bill = total_bill
    
    for p in range(0, num_people):
        unassigned_bill -= per_person_rounded
        dues.append(per_person_rounded)
    
    remainderIncrement = 0
    unassigned_bill = round(unassigned_bill, 2)
    if unassigned_bill > 0:
        remainderIncrement = 0.01
    elif unassigned_bill < 0:
        remainderIncrement = -0.01

    if remainderIncrement != 0:        
        for p in range(0, num_people):
            unassigned_bill -= remainderIncrement
            dues[p] = round(dues[p] + remainderIncrement, 2)            
            if round(unassigned_bill, 2) == 0:
                break
    return dues
