class Animal:
    def __init__(self):
        self.base = "Animal"

    def Base(self):
        print(f" base is {self.base}")

class Cat(Animal):
    def  __init__(self,name):
        self.name = name
        super().__init__()
    
    def Print(self):
        print(" this is ",self.name)

cat_obj = Cat("tiger")
cat_obj.Print()
cat_obj.Base()
