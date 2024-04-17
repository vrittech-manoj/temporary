def isPure(value):
    try:
        int(value)
        return True
    except:
        return False
    
value_str = "kjslksdj"
check = isPure(value_str)
if check == True:
    print(" it is integer")
else:
    print("it is string")
    
#WAP to take age from people , if  age <18 then print "you can not vote" if age is greter than 18 print "you can vote"
#WAP to print below format
    # <12 :"you are child hood"
    # >12-<20 "you are teen agers"
    # >20-<50 "you are adult"
    # >50 print "you are old"


