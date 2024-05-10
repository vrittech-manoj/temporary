class Calculator:
    def __init__(self,a,b):
        print("construction is auto called, value is initializing...")
        self.first_num   = a
        self.second_num = b
    
    def add(self):
        self.display()
        print("Addition:",self.first_num+self.second_num)

    def sub(self):
        print("Subtraction:",self.first_num-self.second_num)

    def display(self):
        print("********************")
        
first_number =  8
second_number = 9

calculator_obj  = Calculator(first_number,second_number)
calculator_obj.add()
calculator_obj.sub()












