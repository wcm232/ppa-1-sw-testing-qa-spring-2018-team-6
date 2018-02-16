def tip_calc(total_bill, num_people):
    total_tip = total_bill * (.15)
    total_bill += total_tip
    per_person = total_bill / num_people
    return per_person
