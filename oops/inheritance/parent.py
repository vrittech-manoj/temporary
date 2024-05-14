class Person: 
    def __init__(self,person_name,person_age):
        
        self.FullDetail()
        print("this is persosn cunstructor")
    
    def FullDetail(self):
        self.detail = self.name+"-"+self.age #it set value to power bank

    def display(self):
        print(f"person name is {self.name} and age is {self.age} and detail is {self.detail}")

class Emp(Person):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("this emp cunstructor")
        Person.__init__(self,name,age)
        # super().__init__(name,age)
    
emp_obj = Emp("ram","19")
# emp_obj.display()

