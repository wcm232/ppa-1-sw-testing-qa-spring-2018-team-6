def calculateTip(sub_total, num_people):
    if type(sub_total) is not int and type(sub_total) is not float:
        raise TypeError()

    if type(num_people) is not int:
        raise TypeError()

    if num_people < 1:
        raise ValueError()    

    total_tip = round(sub_total * 0.15, 2)
    per_person = total_tip / num_people

    dues = []
    per_person_rounded = round(per_person, 2)   
    unassigned_tip = total_tip
    
    for p in range(0, num_people):
        unassigned_tip -= per_person_rounded
        dues.append(per_person_rounded)
    
    remainderIncrement = 0
    unassigned_tip = round(unassigned_tip, 2)
    if unassigned_tip > 0:
        remainderIncrement = 0.01
    elif unassigned_tip < 0:
        remainderIncrement = -0.01

    if remainderIncrement != 0:        
        for p in range(0, num_people):
            unassigned_tip -= remainderIncrement
            dues[p] = round(dues[p] + remainderIncrement, 2)            
            if round(unassigned_tip, 2) == 0:
                break
    return dues
