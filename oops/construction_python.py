class Person:
    #construction attributes initialized.
    def __init__(self,name):
        self.name = "mohan"

    def working(self):
        print(self.name," is working...")

    def study(self):
        print(self.name," is reading")

# first create object
# obj.method name
mohan_person_obj = Person(name="rameshs")
mohan_person_obj.working()
mohan_person_obj.study()

# rahul_person_obj = Person()
# rahul_person_obj.working()
# rahul_person_obj.study()








# def working(name):
#     print(name,"is working...")

# working("mohan")
# working("roshan")




