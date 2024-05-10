class Maths:
    def __init__(self,numbers):
        print("Welcome To Vrit  Math Library.")
        self.list_numbers = numbers
        self.shorted_numbers = sorted(self.list_numbers)

    def getMaximumNumber(self):
        return self.shorted_numbers[-1]
    
    def getMinimumNumber(self):
        return self.shorted_numbers[0]
    

    

    

