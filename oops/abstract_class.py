from abc import ABC,abstractmethod
class Ploygon(ABC):
    
    @abstractmethod
    def noofsides(self):
        pass

class Triangle(Ploygon):

    def noofsides(self):
        print(" i have 3 sides")
    
    def area(self):
        print("calculating area of triangle")


triangle_obj = Triangle()
triangle_obj.area()


class Calculator(ABC):

    @abstractmethod
    def display(sel):
        pass
    
    def addition(self,a,b):
        return a+b 

class MyOwnCalculator(Calculator):
    def display(self):
        print("this is vrit calculator. thanks")


    def subtraction(self,a,b):
        return a-b 
    
my_obj = MyOwnCalculator()
output = my_obj.addition(4,9)
print(output)
# my_obj.display()








