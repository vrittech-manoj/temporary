# Polymorphisms

#)overloading

# in c++,java
# def add(a,b):
#     return  a+b


# def add(a,b,c):
#     return  a+b+c


# def add(a,b,c,d):
#     return  a+b+c+d

# add(2,8,9,76)

# in pytho
# def sum(a,b,c=0):
#     return a+b+c

# output = sum(5,4)
# print(output)



#)overriding
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
    def make_sound(self):
        print("default animal sound")

class Cat(Animal):
    def make_sound(self):
        print("meu meu !!.")

class Dog(Animal):
     def make_sound(self):
        print("bho bho !!.")

class Ant(Animal):
    pass

cat_obj = Cat()
cat_obj.make_sound()









