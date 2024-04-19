#WAP to take user input ,  and print a given number  is prime number or not

# prime  number divisible should less than or equal to 2

# 1->it is prime number(1)
# 2->it is prime(1,2)
# 3->prime(1,3)
# 4->not prime (1,2,4)
# 5->prime (1,5)
# 6->not prime
# 7->prime 
# 8->not prime  
# 9->not prime

# 6 = 6/1(0),6/2(0),6/3(0),6/4(2),6/5(1),6/6(0)

step 1:start 
number = 4#take any number from user (4)

start_number = 1
remainder_count = 0

:top
remainder = number%start_number i.e 4/4 = 0
if remainder == 0:
    remainder_count  = remainder_count +  1 = 2+1= 3

start_number = start_number+1 = 3+1 = 4+1=5
if start_number>number:
    break
goto top

if  remainder_count> 2:
    print(" number  is not prime number")
else:
    print("number  is prime number")

step 2:end

