class Area:

    def __init__(self,l,b):
        self.length = l
        self.breadth = b


    def calculateRectangle(self):#it calculate area of rectangle
        print("area of rectangle: ",self.length*self.breadth)

    
    def calculateSquare(self):#it calculate area of square
        print("area of square :",self.length*self.length)


for i in range(4):
    length = int(input("Enter length#: "))
    breadth = int(input("Enter breaddth: "))
    area_obj = Area(length,breadth)
    area_obj.calculateRectangle()
    area_obj.calculateSquare()