class Calculator:
    def __init__(self,a,b):
        self.fist_num=a
        self.second_num = b
        print(" this is construction")

    def add(self):
        self.output = self.fist_num+self.second_num
    
    def display(self):
        print(f"addition of {self.fist_num},{self.second_num}::", self.output)
    
    def multiply(a,b):
        return a*b

print(Calculator.multiply(4,9))

# calculator_obj = Calculator(10,12)
# add_output = calculator_obj.add()
# calculator_obj.display()

    


