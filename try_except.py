
age = input("Enter your age#>>>")

#try.....except
try:
    age  = int(age)
    if age<18:
        print(" Sorry ! you can not vote ")
    else:
        print(" you can vote ")
except:
    print(" sorry you have given wrong input")
    age = input("Enter your age#>>>")
 

age  = int(age)
if age<18:
    print(" Sorry ! you can not vote ")
else:
    print(" you can vote ")






