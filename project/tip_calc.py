def calculateTip(sub_total, num_people):
    if type(sub_total) is not int and type(sub_total) is not float:
        raise TypeError()

    if type(num_people) is not int:
        raise TypeError()

    if num_people < 1:
        raise ValueError()    

    total_amount = round(sub_total * 1.15, 2)
    per_person = total_amount / num_people

    dues = []
    per_person_rounded = round(per_person, 2)   
    unassigned_amount = total_amount
    
    for p in range(0, num_people):
        unassigned_amount -= per_person_rounded
        dues.append(per_person_rounded)
    
    remainderIncrement = 0
    unassigned_amount = round(unassigned_amount, 2)
    if unassigned_amount > 0:
        remainderIncrement = 0.01
    elif unassigned_amount < 0:
        remainderIncrement = -0.01

    if remainderIncrement != 0:        
        for p in range(0, num_people):
            unassigned_amount -= remainderIncrement
            dues[p] = round(dues[p] + remainderIncrement, 2)            
            if round(unassigned_amount, 2) == 0:
                break
    return dues
