# Polymorphisms

#)overloading


# def sum(a,b,c=0):
#     return a+b+c

# output = sum(5,4)
# print(output)



# #)overriding
# class Calculator:
    
#     def add(self,a,b):
#         print(a+b)
    
#     def sub(self,a,b):
#         print("subtraction :",a-b)
    
# class MyOwnCalculator(Calculator):

#     def add(self,a,b):
#         print("overiding addition ",a+b)

# cal_obj = MyOwnCalculator()
# cal_obj.add(4,5)
# cal_obj.sub(9,5)


class Animal:
    def make_sound():
        print("default animal sound")

class Cat(Animal):
    def make_sound():
        print("meu meu !!.")

class Dog(Animal):
     def make_sound():
        print("bho bho !!.")

class Ant(Animal):
    pass

cat_obj = Ant()
cat_obj.make_sound()









