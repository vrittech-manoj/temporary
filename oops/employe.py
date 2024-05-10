def AddBonus(salary,bonus):
    return salary+bonus

def Fine(ammount,fine_ammount):
    return ammount-fine_ammount


person_name = "ram"
salary = 600
bonus = 2000
fine = 500


salary_after_bonus = AddBonus(salary,bonus)
output_ammount = Fine(salary_after_bonus,fine)
print(f"output of {person_name} salary is :",output_ammount)


