class EmployeSalaryManagement:
    def __init__(self,person_name,salary,bonus,fine):
        print("this is construction...")
        self.employe_name =  person_name
        self.salary = salary
        self.bonus = bonus
        self.fine = fine
    
    def AddBonus(self):
        salary_with_bonus =  self.salary+self.bonus
        return salary_with_bonus

    def Fine(self):#salary with bonus-fine
        output = self.AddBonus()-self.fine
        return  output

person_name = "ram"
salary = 600
bonus = 2000
fine = 500

employe_obj = EmployeSalaryManagement(person_name,salary,bonus,fine)
print("salary with bonus:",employe_obj.AddBonus())
final_salary = employe_obj.Fine()
print(final_salary,"::")


