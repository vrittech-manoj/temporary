

# for i in range(check_number):
#     start_number = i + 1
#     print(i,start_number)

number = int(input("Enter any number "))

start_number = 1
remainder_count = 1
while start_number<=number:
    # print(start_number)
    start_number = start_number+1
    remainder = number%start_number
    if remainder == 0:
        remainder_count = remainder_count + 1
    
if remainder_count>2:
    print(number, " is not prime number")
else:
    print(number," is prime number")