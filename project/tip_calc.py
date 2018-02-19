import math
def tip_calc(cost, num_people):
    total_tip = cost * (.15)
    total_cost = cost + total_tip
    per_person = total_cost / num_people
    #https://stackoverflow.com/questions/6681743/splitting-a-number-into-the-integer-and-decimal-parts-in-python
    split_num = str(per_person).split('.')
    if(len(split_num[1]) <= 2):
        per = [per_person]
        for x in range(0, num_people-1):
            per.append(per_person)
        return per
    else:
        
        total_cost = math.ceil(total_cost*100) / 100
        per_person = round(per_person, 2)
        per = []
        for x in range (0, num_people-1):
            if(x == num_people-1):
                temp = round(per_person,2)
                per.append(temp+ .01)
            else:
                per.append(per_person)

        return per
            
   
